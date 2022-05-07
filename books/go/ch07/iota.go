package main

type MailCategory int

const (
	Uncategorized MailCategory = iota
	Personal
	Spam
	Social
	Ads
)
