// client.ts

import axios from 'axios';

const client = axios.create({
    baseURL: 'https://api.your-backend.com', // Replace with your backend URL
    headers: {
        'Content-Type': 'application/json',
        // Add any other headers here
    }
});

export default client;
