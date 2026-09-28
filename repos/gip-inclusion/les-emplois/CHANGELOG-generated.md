## Changelog : les-emplois (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois a été marqué par une évolution majeure de l'identité visuelle du projet, qui devient "La plateforme de l'inclusion". Les utilisateurs bénéficient d'une expérience enrichie grâce à la création d'un nouvel onglet de synthèse pour le suivi des dossiers, d'une gestion plus fluide des orientations et d'un système d'alertes amélioré (fins de contrat, webinaires). L'outil gagne également en fiabilité avec une piste d'audit renforcée et une meilleure automatisation de la gestion des dossiers salariés.

### Évolutions fonctionnelles
- **Identité et Branding** : Transition complète vers le nouveau nom "La plateforme de l'inclusion" (logos, textes légaux, documentation et API).
- **Suivi des usagers (Vue Synthèse)** : Création d'un nouvel onglet "Synthèse" regroupant les informations essentielles : conseiller référent, dernières candidatures, et informations sur les contrats en cours.
- **Gestion des accompagnements et orientations** :
    - Automatisation de la création d'un accompagnement lors de l'orientation d'un bénéficiaire.
    - Mise en place de "liens magiques" pour permettre aux structures de consulter les détails d'une orientation de manière sécurisée.
    - Ajout de filtres sur les accompagnements et possibilité d'archiver des dossiers.
- **Alertes et notifications** :
    - Mise en place de bannières d'alerte pour signaler les fins de contrat imminentes (pour les employeurs et prescripteurs).
    - Ajout de notifications concernant les opportunités d'immersion.
    - Introduction de bannières d'information pour les webinaires thématiques.
- **Recherche et annuaire** :
    - Amélioration de la recherche d'entreprises.
    - Ajout de la géolocalisation des structures dans l'annuaire professionnel par ville.
- **Gestion des dossiers salariés** : Amélioration de la gestion des erreurs lors de la synchronisation des fiches salariés et automatisation de certains traitements.

### Évolutions techniques
- **Sécurité et Traçabilité** :
    - Implémentation d'une piste d'audit (audit trail) pour suivre les actions sur la plateforme.
    - Sécurisation des processus de fermeture des approbations (passage de requêtes GET à des méthodes sécurisées).
    - Amélioration de la gestion des clés de sécurité (JWKS) avec mise en cache.
- **Architecture et Refactoring** :
    - Nettoyage du code avec la suppression de l'application de recommandations et de certains composants obsolètes.
    - Refactorisation de la logique métier liée aux processus de fermeture des PASS IAE et aux orientations.
- **Données et Statistiques** :
    - Enrichissement des tableaux de bord Metabase avec de nouvelles métriques (délais de transition, données GEIQ, identifiants uniques).
- **Performance et Qualité** :
    - Optimisation des scripts de migration de données (CV).
    - Amélioration de la suite de tests et de la gestion des snapshots.
    - Intégration de nouveaux marqueurs de tracking Matomo pour analyser l'usage des offres et des filtres.

### Autres changements
- **Accessibilité** : Publication d'une déclaration d'accessibilité détaillée.
- **Documentation** : Mise à jour de la documentation technique et des explications relatives au SSO.
- **Interface** : Nombreuses corrections typographiques, ajustements d'espacement et harmonisation de la mise en page pour améliorer la lisibilité.
