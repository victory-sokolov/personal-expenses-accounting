import { useEffect, useState } from "react";

// To Do: Add request caching
const useFetch = (url: string, options?: any) => {

    const [ result, setResult ] = useState(null);
    const [ error, setError ] = useState(null);
    const [ loading, setLoading ] = useState(false);

    useEffect(() => {

        if (!url) return;

        const abortController = new AbortController();
        const signal = abortController.signal;

        const fetchData = async () => {
            setLoading(true);
            try {
                const response = await fetch(url, options);
                const res = await response.json();

                if (!signal.aborted && response.ok) {
                    setResult(res);
                }
            } catch (e: any) {
                if (!signal.aborted) {
                    setError(e);
                }
            } finally {
                if (!signal.aborted) {
                    setLoading(false);
                }
            }

        };
        fetchData();

        return () => {
            abortController.abort();
        };

    }, []);

    return [ result, error, loading ];
};

export default useFetch;