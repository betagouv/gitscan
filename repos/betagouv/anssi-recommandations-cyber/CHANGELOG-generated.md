## Changelog : anssi-recommandations-cyber (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, l'ajout de nouvelles fonctionnalités de recherche et d'analyse de données, ainsi que des corrections de sécurité et des améliorations de l'expérience utilisateur. L'ajout de la collection "Jeopardy" permet d'étendre les capacités de recherche et d'analyse documentaire.

### Évolutions fonctionnelles
- Ajout de la recherche et de l'utilisation de la collection "Jeopardy" pour l'indexation et la recherche documentaire.
- Possibilité de récupérer les "chunks" originaux associés aux "chunks" Jeopardy.
- Affichage d'un lien "En savoir plus" lorsque la source documentaire est une page HTML.
- Amélioration du prompt pour le rendre plus permissif et améliorer la qualité des réponses.
- Ajout d'un notebook pour comparer les collections d'indexation et Jeopardy.
- Possibilité de lister les documents d'une collection dans un dataframe via leurs noms.
- Affichage des données d'une collection.
- Ajout d'un champ de saisie pour la clé d'API dans l'interface.
- Ajout d'une analyse pour les collections avec des documents sans "chunks".
- La reformulation est désormais obligatoire.
- Ajout du suivi Matomo sur le bouton de copie de réponse, avec obtention du consentement de l'utilisateur.

### Évolutions techniques
- Séparation des environnements de développement et de production.
- Vérification de la présence des variables d'environnement nécessaires au démarrage du serveur.
- Gestion améliorée des erreurs : remontée des messages d'erreur originaux et affichage de messages d'erreur génériques.
- Amélioration de la gestion des erreurs liées à la recherche documentaire.
- Mise en place d'un workflow de déploiement sur l'environnement de production.
- Utilisation d'une base de données mémoire et d'un Sentry mémoire lors de l'exécution des tests.
- Clarification des messages d'erreur.
- Correction d'une typo ("appriécé" corrigé en "apprécié").
- Mise à jour de plusieurs dépendances : `dompurify`, `requests`, `svelte`, `pytest`, `cryptography`.

### Autres changements
- Suppression du tag "conversation" devenu obsolète.
- Ajout d'un fichier de configuration Renovate.
- Ajout de logs au démarrage pour expliciter la configuration utilisée.
- Nettoyage du notebook d'interaction avec Albert.
- Récupération des collections par ordre de création chronologique décroissant.
- Modification du wording sur l'interface utilisateur.
