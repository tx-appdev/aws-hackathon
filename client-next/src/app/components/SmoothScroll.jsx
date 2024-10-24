"use client";

import { ReactLenis } from 'lenis/react';

function SmoothScroll({
    children,
}) {
    return (
        <ReactLenis root options={{
            duration: 1.2,
        }}>
            { children }
        </ReactLenis>
    )
}

export default SmoothScroll;