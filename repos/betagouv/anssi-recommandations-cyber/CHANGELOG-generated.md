## Changelog : anssi-recommandations-cyber (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, l'ajout de fonctionnalités de recherche et d'analyse de données, ainsi que la préparation du déploiement en production. Des corrections de bugs et des améliorations de la gestion des erreurs ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout de la recherche dans la collection "Jeopardy" et possibilité d'appeler cette collection depuis le service.
- Possibilité de récupérer les chunks originaux associés aux chunks Jeopardy.
- Amélioration du prompt utilisé pour la recherche, le rendant plus permissif.
- Affichage d'un lien "En savoir plus" lorsque la source documentaire est une page HTML.
- Possibilité de lister les documents d’une collection dans un dataframe via leurs noms.
- Ajout d'un notebook pour comparer les collections d’indexation et Jeopardy.
- Affichage des données d'une collection.
- Ajout d'un champ de saisie pour la clé d'API dans l'interface.
- Analyse d'une collection avec les documents sans chunks.

### Évolutions techniques
- Préparation du déploiement en production avec un workflow dédié et l'obligation de passer par la démo avant la mise en production.
- Séparation des environnements de développement et de production.
- Vérification de la présence des variables d'environnement nécessaires au démarrage du serveur.
- Gestion améliorée des erreurs :
    - Retour d'une erreur HTTP 500 en cas d'impossibilité de communiquer avec Albert.
    - Remontée du message d'erreur original renvoyé par Albert.
    - Clarification des messages d'erreur.
    - Généralisation de la recherche pour un comportement plus homogène.
- Utilisation d'une base de données mémoire et d'un Sentry mémoire lors de l'exécution des tests.
- Correction d'une typo ("appriécé" -> "apprécié").
- Obtention du consentement pour le suivi Matomo.

### Autres changements
- Ajout de logs au démarrage pour expliciter la configuration utilisée.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (dompurify, requests, svelte) via Dependabot.
- Renommage de `ErreurRechercheGuidesAnssi` en `ErreurRechercheDocuments`.
- Récupération des collections par ordre de création chronologique décroissant.
- Modification du wording de certains éléments de l'interface.
