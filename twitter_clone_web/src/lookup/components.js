export const FetchTweets = async () => {
    const res = await fetch('http://localhost:8000/api/tweets')
    if (res.status === 200) {
        const data = await res.json()
        return data
    } else console.log({'message': 'Error while loading tweets'}, res.status)
}