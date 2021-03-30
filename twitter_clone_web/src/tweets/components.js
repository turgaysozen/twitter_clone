import React, { useEffect, useState } from 'react'
import { FetchTweets } from '../lookup'

export const TweetList = () => {
    const [tweets, setTweets] = useState([])
    useEffect(() => {
        async function loadTeets() {
            const res = await FetchTweets()
            setTweets(res)
        }
        loadTeets()
    }, [])

    return tweets.map((item) => {
        return <Tweet key={item.id} tweet={item} className='my-5 py-5 border bg-white text-dark' />
    })
}

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
