## Changelog : anssi-recommandations-cyber (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des réponses fournies par Albert, notamment en priorisant les paragraphes "maîtrisés" et en affinant le prompt.  Des améliorations significatives ont également été apportées à l'infrastructure, avec la mise en place d'un déploiement en production, une meilleure gestion des erreurs et l'ajout de tests.  Enfin, l'interface utilisateur a été enrichie avec une page FAQ en cours de construction et l'ajout de Matomo pour le suivi des actions utilisateurs.

### Évolutions fonctionnelles
- Ajout d'une page FAQ en cours de construction. [#1234](https://github.com/betagouv/anssi-recommandations-cyber/issues/1234)
- Amélioration de la qualité des réponses : priorisation des paragraphes "maîtrisés" et filtrage des réponses maîtrisées.
- Amélioration du prompt pour une plus grande permissivité.
- Affichage d'un lien "En savoir plus" lorsque la source documentaire est une page HTML.
- Possibilité de lister les documents d'une collection dans un dataframe via leurs noms.
- Ajout de la recherche Jeopardy et de la possibilité d'appeler la collection Jeopardy depuis le service.
- Correction d'une typo ("appriécé" corrigé en "apprécié").

### Évolutions techniques
- Mise en place d'un workflow de déploiement sur l'environnement de production.
- Séparation des environnements de développement et de production.
- Vérification de la présence des variables d'environnement nécessaires au démarrage du serveur.
- Gestion améliorée des erreurs :
    - Retour d'une erreur HTTP 500 en cas d'impossibilité de communiquer avec Albert.
    - Remontée du message d'erreur original plutôt qu'une interprétation.
    - Génération d'un message d'erreur générique plutôt qu'un message technique.
    - Lève désormais une exception Albert.
- Amélioration de la gestion des erreurs lors de la recherche documentaire.
- Utilisation d'une base de données mémoire et d'un Sentry mémoire lors de l'exécution des tests.
- Ajout d'un singleton pour charger le fichier de mapping.
- Résolution de l'ID de réponse via un mapping JSON au lieu de le stocker en métadonnée.
- Extraction d'un `ParagrapheReponseMaitrisee` pour faciliter les réponses retournées.
- Suppression des informations "en dur" du prompt.
- Ajout de logs au démarrage pour expliciter la configuration utilisée.
- Mise à jour de la dépendance pytest suite à une alerte de sécurité.
- Mise à jour des dépendances dompurify, python-dotenv et cryptography suite à des alertes de sécurité.

### Autres changements
- Ajout du tracking Matomo sur le bouton de copie de réponse.
- Ajout d'un notebook pour comparer les collections d’indexation et jeopardy.
- Ajout d’un champ de saisi pour la clef d’API dans le notebook.
- Ajout de l’analyse d’une collection avec les documents sans chunks.
- Ajout de la configuration de la collection jeopardy.
- Ajout du fichier de configuration Renovate.
- Nettoyage du notebook d’interaction avec Albert.
- Obtention du consentement du suivi Matomo.
- Les collections sont maintenant récupérées par ordre de création chronologique décroissant.
- Suppression du tag conversation devenu obsolète.
- De nombreuses mises à jour de dépendances ont été effectuées via Renovate (voir les commits pour plus de détails).
