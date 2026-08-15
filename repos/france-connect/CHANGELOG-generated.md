# Synthèse d'activité : france-connect (du 11/05 au 18/05)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'amélioration de l'expérience utilisateur et l'élargissement des capacités d'accès au service. Des optimisations majeures ont été apportées au tableau de bord utilisateur, notamment pour une utilisation mobile plus fluide et une meilleure gestion des sessions. L'ajout de liens de support contextuels sur les pages d'erreur et l'intégration de nouveaux éléments visuels (logo Yris) visent à simplifier le parcours des usagers et à faciliter l'assistance. Par ailleurs, l'ouverture via l'eIDASBridge permet d'intégrer de nouveaux prestataires de services, renforçant ainsi l'écosystème [sources](/repos/france-connect/sources).

## Sécurité
- Renforcement de la protection de la vie privée par la suppression de données non nécessaires (claims "phone_number" et "address") dans FranceConnect+ [sources](/repos/france-connect/sources).
- Amélioration de l'isolation réseau via la séparation des consommateurs MongoDB selon le niveau d'assurance [sources](/repos/france-connect/sources).

## Autres changements notables
- Amélioration de la traçabilité et du diagnostic grâce à l'ajout de logs métier détaillés (incluant l'IP et le port client) [sources](/repos/france-connect/sources).
- Refactorisation de l'architecture du code pour optimiser le partage de composants et la maintenabilité [sources](/repos/france-connect/sources).
- Renforcement de la qualité logicielle par l'implémentation de tests BDD sur les notifications et l'historique de connexion [sources](/repos/france-connect/sources).

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Évolutions centrées sur l'expérience utilisateur, la sécurité des données et la robustesse technique de l'infrastructure.
