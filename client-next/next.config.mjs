/** @type {import('next').NextConfig} */
import withVideos from 'next-videos';

const nextConfig = {
    trailingSlash: true,
    webpack(config) {
        config.module.rules.push({
          test: /\.svg$/,
          use: [{ loader: "@svgr/webpack", options: { icon: true } }],
        });
        return config;
      },
};

const config = withVideos({
    ...nextConfig,
});

export default config;
