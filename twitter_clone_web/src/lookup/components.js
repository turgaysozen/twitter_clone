// fetch tweets 
export const FetchTweets = async () => {
    const res = await fetch('http://localhost:8000/api/tweets')
    if (res.status === 200) {
        const data = await res.json()
        return data
    } else console.log({ 'message': 'Error while loading tweets' }, res.status)
}

// get cookie for csrftoken
const getCookie = (name) => {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// post tweet
export const createTweet = async (newTweet) => {
    const csrftoken = getCookie('csrftoken')
    const data = {
        content: newTweet,
    }
    const url = 'http://localhost:8000/api/tweets/create'
    const res = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    return res
}

export const actionLike = async (id, action) => {
    const csrftoken = getCookie('csrftoken')
    const data = {
        id: id,
        action: action
    }
    const url = 'http://localhost:8000/api/tweets/action'
    const res = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    return res
}
