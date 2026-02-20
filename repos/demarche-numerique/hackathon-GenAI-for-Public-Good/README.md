# Hackathon GenAI for Public Good 🤖  

📙 **Retrouvez le Guide du participant en cliquant** [ici](https://alliance.numerique.gouv.fr/hackathon/participant-guide-fr/)  


#### 🛠 Track 2 : Cas d'Usage à Fort Impact avec des APIs  

### 📝 Informations à renseigner pour l’évaluation  

Merci de compléter ce README avec les éléments suivants :  

##### 🏆 Critères d'évaluation  
| Critère            | Description | Poids (%) |
|--------------------|-------------|-----------|
| 🎯 **Pertinence**  | La solution répond-elle à un défi clair du service public ? | 25 |
| 📈 **Impact**      | Les résultats attendus sont-ils significatifs et mesurables ? | 25 |
| 🔧 **Faisabilité** | L’implémentation du MVP est-elle réaliste ? | 25 |
| 🌍 **Scalabilité** | La solution est-elle adaptable et conçue comme un bien commun numérique ? | 25 |

---

https://github.com/user-attachments/assets/7a7207e4-8915-4671-897a-1d6ccdadc67c

**Pertinence**

Chaque année, ce sont près de 10 000 démarches administratives qui sont créées sur l'outil Démarches simplifiées, pour lesquelles 4 millions de dossiers sont déposés. La bonne qualité de ces démarches est une nécessité, tant pour l'administration elle même, qui est en charge du traitement des demandes, que pour les usagers dans un souci de simplification administrative. 
Si Démarches simplifiées met en oeuvre tout un ensemble d'actions visant à permettre aux administrations d'avoir les clés utiles à l'élaboration de démarches de qualité, et ce en parallèle des travaux de la DITP autour de la simplification des démarches administratives, force est de constater à ce jour qu'il demeure des défauts de qualité plus ou moins majeurs sur les démarches disponibles.
Aussi, il est proposé d'intégrer au sein même de DS l'utilisation de technologies de LLM, qui se traduit par un outil d'assitance à l'amélioration de la qualité des démarches. Concrètement, cet assistant propose aux administrateurs des modifications dans la structure et la formulation des champs du formulaire, en restant naturellement maître sur l'intégration des propositions.

**Impact**
La solution proposée peut être déployée en deux temps, (i) en continue sur toutes les nouvelles démarches créées (40 par jour), puis (ii) à l'ensemble des démarches disponibles sur Démarches simplifiées (près de 40 000).
Dans le cadre de l'élaboration de la solution, un ensemble de règles liées à la qualité ont été établies (en lien étroit avec les guides de recommandations de la DITP), permettant de qualifier les défauts de qualité. Il sera ainsi aisé dès le premier déploiement du dispositif d'assistante, d'en mesurer les impacts concrets sur la qualité des démarches.

**Faisabilité**
L'implémentation du MVP a pu être déjà expérimenté dans le cadre du hackathon : https://github.com/demarches-simplifiees/demarches-simplifiees.fr/pull/11284. Dans ce cadre nous avons testé la solution principalement sur une démarche réelle.

**Scalabilité**
Le code du dispositif d'assistance, ainsi que le LLM utilisé sont tout deux en opensource.

____
