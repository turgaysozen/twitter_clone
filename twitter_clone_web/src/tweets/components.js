import React, { useEffect, useState } from 'react'
import { FetchTweets, createTweet, actionLike } from '../lookup'

// 'create new tweet component',it handles form by onsubmit method
export const TweetComponent = (props) => {
    const textAreaRef = React.createRef()
    const [newTweets, setNewTweets] = useState([])
    const handleSubmit = async (event) => {
        event.preventDefault()
        const newTweet = textAreaRef.current.value
        if (newTweet) {
            let tempNewTweets = [...newTweets]
            const res = await createTweet(newTweet)
            const res_data = await res.json()
            if (res.status === 201) {
                tempNewTweets.unshift({
                    content: res_data["content"],
                    id: res_data["id"],
                    likes: res_data["likes"],
                })
                textAreaRef.current.value = ''
                setNewTweets(tempNewTweets)
            }
        } else alert('Enter a tweet!!')
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
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweetsInit, tweets]) // dependencies are new tweet and init tweet list

    // init tweet list before create a new tweet
    useEffect(() => {
        const loadTeets = async () => {
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
    const handleClick = async (event) => {
        event.preventDefault()
        if (action.type === 'like') {
            if (likes === 0) {
                const res = await actionLike(tweet.id, 'like')
                const data = await res.json()
                setLikes(data.likes)
            } else if (likes === 1) {
                const res = await actionLike(tweet.id, 'unlike')
                const data = await res.json()
                setLikes(data.likes)
            }
            // if (userLike) {
            //     setLikes(likes - 1)
            //     setUserLike(false)
            // } else {
            //     setLikes(likes + 1)
            //     setUserLike(true)
            // }
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
            {/* <ActionBtn tweet={tweet} action={{ type: 'unlike', display: 'Unlike' }} /> */}
            <ActionBtn tweet={tweet} action={{ type: 'retweet', display: 'Retweet' }} />
        </div>
    </div>
}
