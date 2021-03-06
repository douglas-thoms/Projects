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
library(titanic)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
        df = data.frame(Titanic)
        filtered.sex <- reactive({
                df %>%
                        filter((Sex %in% input$sex)) 
                        
   })   
        filtered.age <- reactive({
                df %>%
                        filter((Age %in% input$age))
   })  
        
        output$barplot1 <- renderPlot(({
                ggplot(data=filtered.sex(),aes(x=Survived,y=Freq,fill=Class))+
                        geom_bar(stat='identity',width = .8) +
                        ggtitle("Survival by Sex") +
                        theme(plot.title = element_text(hjust = 0.5))
        }))
        output$barplot2 <- renderPlot(({
                ggplot(data=filtered.age(),aes(x=Survived,y=Freq,fill=Class)) +
                        geom_bar(stat='identity', width = .8) +
                        ggtitle("Survival by Age") +
                        theme(plot.title = element_text(hjust = 0.5))
        }))
        
        output$table <- renderDataTable(df)
})
