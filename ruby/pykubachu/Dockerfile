FROM ruby:2.6.3-alpine3.9

WORKDIR /app
EXPOSE 8080
CMD [ "./app.rb" ]

COPY Gemfile .
RUN bundle install

COPY images/ ./images

COPY app.rb .
