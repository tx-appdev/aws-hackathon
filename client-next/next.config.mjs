/** @type {import('next').NextConfig} */
import withVideos from 'next-videos';

const nextConfig = {
    trailingSlash: true,
};

const config = withVideos({
    ...nextConfig,
});

export default config;
