<?php
// you can write to stdout for debugging purposes, e.g.
// print "this is a debug message\n";

function solution($N)
{
    // write your code in PHP5.5
    $arr = str_split(decbin($N));

    $ones =  array_values(array_filter(array_map(function ($keys, $var) {
        if ($var == 1) {
            return $keys;
        }
        return 0;

    }, array_keys($arr), $arr), function ($var) {
        return $var;
    }));

    $gaps = [];

    foreach ($ones as $key => $value) {
        if ($key == 0) {
            array_push($gaps, $value - 1);
        } else {
            array_push($gaps, $value- $ones[$key-1] - 1);
        }
    }

    return empty($gaps) ? 0 : max($gaps);
}

echo solution(529);
