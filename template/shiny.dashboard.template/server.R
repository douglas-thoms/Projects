#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinydashboard)
library(ggplot2)
library(dplyr)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
        peak = read.csv("~/Training/Projects/template/shiny.dashboard.template/peak.hours.data.csv")
        filtered.peak <- reactive({
                peak %>%
                        filter((ISO %in% input$iso) & 
                                       (top20.actual.peak.day == 1) & (actual.peak.hour == 1)) 
                        
   })   
        top.peaks <- reactive({
                peak %>%
                        filter(
                                (annual.actual.load.rank <= input$num) & 
                                       (ISO %in% input$iso) & (actual.peak.hour==1) &
                                (year == input$year) & (forecaster == input$forecaster)
                                ) %>%
                        select(date,year,hour.start,annual.actual.load.rank,annual.same.day.forecast.load.rank,hit)
   })  
        
        graph.data = read.csv("~/Training/Projects/template/shiny.dashboard.template/peak.captured.summary.csv")
        filtered.graph.data <- reactive({
                graph.data %>%
                        filter(ISO %in% input$iso)

   })  
        output$barplot1 <- renderPlot(({
                ggplot(data=filtered.peak(),aes(x=hour.start,fill=month))+
                        geom_bar(stat='count',width = .8) + facet_wrap(~year)
        }))
        output$barplot2 <- renderPlot(({
                ggplot(data=filtered.graph.data(),aes(x=ISO,y=Number.of.Peaks.Captured,fill=Forecaster)) +
                        geom_bar(stat='identity', position='dodge') + facet_wrap(~Year)
        }))
        
        output$table <- renderDataTable(top.peaks())
})
