## Changelog : les-emplois (30 derniers jours, au 11 septembre 2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes dans la gestion des parcours d'accompagnement, notamment avec l'ajout de fonctionnalités de création, d'édition et d'archivage des missions. L'interface a été largement modernisée et réorganisée pour mieux servir les différents acteurs (GEIQ, OPCS, employeurs), tandis que les outils de pilotage (Metabase) ont été enrichis pour offrir une meilleure visibilité sur les données.

### Évolutions fonctionnelles
- **Gestion des accompagnements :**
    - Mise en place d'un cycle de vie complet pour les missions (création, modification, archivage et gestion des fins de contrat).
    - Ajout de nouveaux filtres pour faciliter la recherche (fin de parcours, fin de contrat, membres de l'organisation).
    - Création d'onglets dédiés pour les conseillers et amélioration de l'affichage des informations de contact.
- **Nouveaux acteurs et périmètres :**
    - Intégration de fonctionnalités spécifiques pour les GEIQ et les OPCS (affichage des missions et filtres dédiés).
    - Ajout de nouveaux éléments de navigation pour les organisations accréditées.
- **Expérience utilisateur et Interface :**
    - Réorganisation complète des menus de navigation et de la structure de l'interface.
    - Mise à jour de l'identité visuelle (branding) et harmonisation des libellés.
    - Ajout de nouveaux éléments au tableau de bord (cartes "Mon Récap", alertes thématiques, compteurs de fin de contrat).
- **Processus métier et Administration :**
    - Amélioration de la gestion des orientations (utilisation de liens magiques, gestion des pièces jointes et des erreurs).
    - Optimisation du processus de clôture des PASS IAE (formulaires internes, notifications aux candidats).
    - Ajout de la géolocalisation des structures dans l'annuaire professionnel (interface admin).
- **Pilotage et Statistiques :**
    - Enrichissement des tableaux de bord Metabase avec de nouvelles métriques (délais de transition, données GEIQ, identifiants uniques).

### Évolutions techniques
- **Architecture et Backend :**
    - Refactorisation de la logique métier (approbations, règles IAE, recommandations) pour plus de modularité.
    - Automatisation de tâches via des jobs cron (archivage des missions, détection de fichiers manquants).
    - Optimisation des performances (réduction des appels en templates, accélération des tâches de migration).
    - Amélioration de la gestion des données (horodatages automatiques, verrouillage des enregistrements pour les réponses ASP).
- **Sécurité et Accès :**
    - Généralisation de l'authentification via ProConnect pour les professionnels et les institutions.
    - Renforcement de la sécurité des API (ajout de nouveaux scopes pour les endpoints h2a et RQTH).
    - Amélioration de la traçabilité via l'ajout d'un identifiant de navigateur dans les logs d'audit.
- **Qualité logicielle :**
    - Refonte importante de la suite de tests (utilisation de factories, paramétrage des tests).
    - Amélioration de la robustesse des tests de rendu et de typographie.

### Autres changements
- **Documentation :** Amélioration des instructions de configuration pour l'environnement de développement local.
- **Maintenance et Nettoyage :**
    - Nettoyage intensif des templates (correction des espacements, de la typographie et des caractères spéciaux).
    - Suppression de modules et d'applications obsolètes (GPS, recommandations).
