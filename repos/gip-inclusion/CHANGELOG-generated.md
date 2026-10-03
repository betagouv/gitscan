# Synthèse d'activité : gip-inclusion (du 29/06 au 01/10)

## Résumé de l'activité
L'activité récente de l'organisation a été marquée par des transformations d'identité majeures, notamment le rebranding de "La plateforme de l'inclusion" ([les-emplois](/repos/gip-inclusion/les-emplois)) et de "Match Europe" ([grist-custom-forms](/repos/gip-inclusion/grist-custom-forms)). Ces évolutions s'accompagnent d'une amélioration significative de l'expérience utilisateur, avec des tableaux de bord enrichis ([immersion-facile](/repos/gip-inclusion/immersion-facile), [eures-beta](/repos/gip-inclusion/eures-beta)) et des outils de recherche plus intelligents et intuitifs ([data-inclusion](/repos/gip-inclusion/data-inclusion), [dora](/repos/gip-inclusion/dora)).

Parallèlement, l'organisation a franchi des étapes technologiques clés pour soutenir sa croissance. La migration vers Airflow 3 ([pilotage-airflow](/repos/gip-inclusion/pilotage-airflow)) et l'adoption de déploiements en mode serverless ([fluo-proto](/repos/gip-inclusion/fluo-proto)) renforcent la fiabilité des flux de données et la scalabilité des services, garantissant ainsi une plateforme plus robuste pour les utilisateurs finaux.

## Sécurité
- **Renforcement de l'authentification et des accès** : Amélioration de la gestion des secrets pour le protocole OIDC ([inclusion-connect](/repos/gip-inclusion/inclusion-connect), [les-emplois](/repos/gip-inclusion/les-emplois)) et mise en place de clés API spécifiques par client ([autometa-jobs](/repos/gip-inclusion/autometa-jobs)).
- **Protection des interfaces et des données** : Renforcement de la politique de sécurité (CSP) pour les intégrations en iframe ([plateforme-accueil](/repos/gip-inclusion/plateforme-accueil)) et suppression des mots de passe codés en dur dans les environnements de prototype ([fluo-proto](/repos/gip-inclusion/fluo-proto)).
- **Traçabilité et audit** : Implémentation de systèmes de pistes d'audit pour assurer le suivi des actions critiques ([les-emplois](/repos/gip-inclusion/les-emplois), [api-relay-cnav](/repos/gip-inclusion/api-relay-cnav)).

## Autres changements notables
- **Migrations d'infrastructure majeures** : Passage à Airflow 3 ([pilotage-airflow](/repos/gip-inclusion/pilotage-airflow)), migration vers SeaweedFS pour le stockage ([dora](/repos/gip-inclusion/dora)) et adoption de RustFS pour l'optimisation système ([autometa](/repos/gip-inclusion/autometa)).
- **Internationalisation** : Mise en place de la gestion multi-langues (i18n) pour le site institutionnel ([site-institutionnel-2025](/repos/gip-inclusion/site-institutionnel-2025)).
- **Modernisation du déploiement** : Transition vers une architecture de conteneurs serverless pour les prototypes ([fluo-proto](/repos/gip-inclusion/fluo-proto)).

## Dépôts les plus actifs
- [pilotage-airflow](/repos/gip-inclusion/pilotage-airflow) : Migration majeure de l'infrastructure et enrichissement massif des modèles de données.
- [dora](/repos/gip-inclusion/dora) : Refonte de l'expérience utilisateur pour les gestionnaires et évolutions importantes de l'infrastructure de stockage.
- [grist-custom-forms](/repos/gip-inclusion/grist-custom-forms) : Rebranding vers Match Europe et optimisation des processus de matching et de candidatures.
- [les-emplois](/repos/gip-inclusion/les-emplois) : Transformation identitaire et renforcement de la sécurité et de la traçabilité.
- [immersion-facile](/repos/gip-inclusion/immersion-facile) : Amélioration des tableaux de bord et des fonctionnalités de gestion des conventions.
