import React, { useEffect, useState } from 'react'
import { FetchTweets } from '../lookup'

// 'create new tweet component',it handles form by onsubmit method
export const TweetComponent = (props) => {
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])
    const handleSubmit = (event) => {
        event.preventDefault()
        const newTweet = textAreaRef.current.value
        let tempNewTweets = [...newTweets]
        tempNewTweets.unshift({
            content: newTweet,
            id: 123,
            likes: 0
        })
        setNewTweets(tempNewTweets)
        textAreaRef.current.value = ''
    }

    return <div className={props.className}>
        <div className='col-12 mb-3'>
            <form onSubmit={handleSubmit}>
                <textarea rows='5' ref={textAreaRef} className='form-control' name='tweet'>

                </textarea>
                <button className='btn btn-primary my-3' type='submit'>Tweet</button>
            </form>
            <TweetList newTweets={newTweets} />
        </div>
    </div>
}

// list all tweet list component
export const TweetList = (props) => {
    const [tweetsInit, setTweetsInit] = useState([]) // for init tweet list
    const [tweets, setTweets] = useState([]) // for last tweet list

    // last tweet list after create a new tweet
    useEffect(() => {
        const final = [...props.newTweets].concat(tweetsInit)
        if(final.length !== tweets.length){
            setTweets(final)
        }
    }, [props.newTweets, tweetsInit]) // dependencies are new tweet and init tweet list

    // init tweet list before create a new tweet
    useEffect(() => {
        async function loadTeets() {
            const res = await FetchTweets()
            setTweetsInit(res)
        }
        loadTeets()
    }, []) // there are no dependencies (because it lists init tweet list)

    return tweets.map((item) => {
        return <Tweet key={item.id} tweet={item} className='my-5 py-5 border bg-white text-dark' />
    })
}

// action button component for like, unlike and retweet
export const ActionBtn = (props) => {
    const { tweet, action } = props
    const [likes, setLikes] = useState(tweet.likes ? tweet.likes : 0)
    const [userLike, setUserLike] = useState(tweet.userLike ? true : false)
    const className = 'btn btn-primary btn-sm'
    const actionDisplay = action.display ? action.display : 'Action'
    const handleClick = (event) => {
        event.preventDefault()
        if (action.type === 'like') {
            if (userLike) {
                setLikes(likes - 1)
                setUserLike(false)
            } else {
                setLikes(likes + 1)
                setUserLike(true)
            }
        }
    }
    const display = action.type === 'like' ? `${likes} ${actionDisplay}` : actionDisplay
    return <button className={className} onClick={handleClick}>{display}</button>
}

// single tweet item component with has action buttons
export const Tweet = (props) => {
    const { tweet } = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{tweet.id} - {tweet.content}</p>
        <div className='btn btn-group'>
            <ActionBtn tweet={tweet} action={{ type: 'like', display: 'Likes' }} />
            <ActionBtn tweet={tweet} action={{ type: 'unlike', display: 'Unlike' }} />
            <ActionBtn tweet={tweet} action={{ type: 'retweet', display: 'Retweet' }} />

        </div>
    </div>
}
