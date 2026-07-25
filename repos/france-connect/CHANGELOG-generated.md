# Synthèse d'activité : france-connect (du 01/05 au 18/05/2026)

## Résumé de l'activité
L'activité récente de FranceConnect s'est concentrée sur l'amélioration de l'expérience utilisateur et de la sécurité de la plateforme. Des améliorations ont été apportées au tableau de bord utilisateur, notamment pour une meilleure gestion des sessions et une interface plus claire sur mobile. La plateforme s'ouvre également à l'intégration de prestataires de services avec des exigences de sécurité variées via l'eIDASBridge. Ces évolutions visent à faciliter l'utilisation de FranceConnect pour les citoyens et à élargir son écosystème de partenaires.

## Sécurité
- Ajout de la source IP du client et du port aux logs métier de FranceConnect+ pour une meilleure traçabilité. [sources](/repos/france-connect/sources)
- Possibilité de connecter des prestataires de services ayant des exigences de sécurité plus faibles via l'eIDASBridge. [sources](/repos/france-connect/sources)

## Autres changements notables
- Refactorisation de la hiérarchie des dossiers pour améliorer le partage de code entre les applications React. [sources](/repos/france-connect/sources)
- Séparation des consommateurs MongoDB par plateforme pour une meilleure isolation réseau. [sources](/repos/france-connect/sources)
- Suppression des claims inutilisés "phone_number" et "address" dans FranceConnect+. [sources](/repos/france-connect/sources)

## Dépôts les plus actifs
- [sources](/repos/france-connect/sources) : Amélioration continue de l'expérience utilisateur, de la sécurité et de la maintenabilité du code, avec un focus sur le tableau de bord utilisateur et FranceConnect+.
