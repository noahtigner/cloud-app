const fetchData = async (url, params={}) => {
    const call = await fetch(url, params);
    const response = await call;
    const data = await call.json();
    if (!response.ok || !data.success) {
        throw new Error("\n" + data.message + "\n" + url);
    }
    else {
        let token = response.headers.get("x-access-tokens");
        if(token !== null) {
            console.log(token);
            localStorage.setItem('token', token);
        }
        
    }
    return data;
};

export default fetchData;