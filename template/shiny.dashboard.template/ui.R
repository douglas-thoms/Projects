#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinydashboard)

#new goal - 10 peak table comparison, can chose actual or forecast

# Define UI for application that draws a histogram
shinyUI(
                
        
        
        dashboardPage(
                dashboardHeader(title="Controls"),
                dashboardSidebar(
                        
                        menuItem(selectInput("sex", "Choose a Sex:",
                                                        c("Female" = "Female",
                                                          "Male" = "Male"))),
                        menuItem(selectInput("age", "Choose Age:",
                                                        c("Child" = "Child",
                                                          "Adult" = "Adult")))

                                
                ),
                dashboardBody(
                        fluidPage( titlePanel("Titanic"),
                                fluidRow(
                                        box(plotOutput("barplot1")),
                                        box(plotOutput("barplot2"))
                                ),
                                
                                fluidRow(
                                        dataTableOutput('table'))
                        
                        )

       )

   )
   
)