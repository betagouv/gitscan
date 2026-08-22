## Changelog : histologe (30 derniers jours, au 21/08/2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'optimisation de la gestion des dossiers et des signalements, notamment via l'automatisation de certaines clôtures et une meilleure collaboration avec les partenaires. L'interface de gestion a également été enrichie pour faciliter le travail des agents, avec des messages d'erreur plus clairs et une meilleure visibilité des informations importantes.

### Évolutions fonctionnelles
- **Gestion des signalements et des dossiers** :
    - Amélioration des capacités de clôture : clôture automatique des dossiers inactifs [#6178], clôture par un RT [#6186], clôture pour le compte d'un partenaire [#6124] et gestion spécifique de la clôture pour la "Démarche Accélérée" [#6162, #6153].
    - Possibilité de mentionner un partenaire directement dans un signalement [#6176].
    - Partage des informations de clôture d'injonction avec les bailleurs [#6185, #6193].
    - Nouvelle fonctionnalité d'importation de l'historique des arrêtés dans la gestion du territoire [#6133].
- **Interface et Backoffice** :
    - Ajout d'un bandeau de communication dans l'interface d'administration [#6191].
    - Amélioration de l'interface utilisateur pour la saisie des notes personnelles [#6184, #6190].
    - Optimisation des messages d'erreur pour l'import d'arrêtés [#6189] et les problèmes de jeton CSRF [#6188].
- **Corrections de bugs** :
    - Résolution de problèmes de filtrage dans la liste des signalements [#6214].
    - Correction d'erreurs d'affichage des communications in-app [#6239] et de doublons de données (contraintes d'intégrité) [#6205].
    - Correction d'un problème de score nul via l'API [#6172] et ajustement du type de suivi pour les conclusions de visite [#6187].

### Évolutions techniques
- **Sécurité et API** :
    - Renforcement de la gestion des limites de requêtes (rate limiting) et implémentation de la régénération des jetons expirés [#6218, #6232].
    - Amélioration de la traçabilité et du diagnostic des erreurs 401 (ajout de Correlation-ID et diagnostic d'IP sortante) [#6228].
    - Publication d'un postmortem suite à une vulnérabilité signalée via YesWeHack [#6223].
- **Architecture et Maintenance** :
    - Mise à jour du framework Symfony [#6168].
    - Migration technique des adresses des signalements au sein du socle [#6202].
    - Investigations techniques sur les erreurs 400 de l'API RIAL [#6235].
