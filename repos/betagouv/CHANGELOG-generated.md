# Synthèse d'activité : betagouv (du 24/04 au 24/05)

## Résumé de l'activité
L'activité de l'organisation betagouv au cours des dernières semaines a été marquée par une forte concentration sur l'amélioration de la qualité des données, la sécurité et l'expérience utilisateur de ses nombreux outils et services. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et assurer la stabilité. Des efforts significatifs ont été déployés pour moderniser les infrastructures, notamment avec des migrations vers des versions plus récentes de langages et de frameworks (Symfony, Next.js, Node.js).  Plusieurs projets ont également vu l'ajout de nouvelles fonctionnalités, comme l'intégration de systèmes d'authentification plus robustes (ProConnect, Ademe Connect), l'amélioration des interfaces utilisateur (maestro, mon-service-securise) et l'ajout de nouvelles capacités d'analyse et de reporting (turgot-metabase, mes-aides-analytics). L'accent a été mis sur la simplification des processus pour les utilisateurs, notamment dans les domaines de la gestion des subventions, de l'aide au logement et de l'accès aux services publics.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour de sécurité importantes :
- [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) : Correction d'une vulnérabilité critique dans la gestion des sessions.
- [lab-anssi-lib](/repos/betagouv/lab-anssi-lib) : Mise à jour de plusieurs dépendances pour corriger des vulnérabilités.
- [gestion-des-subventions-locales](/repos/betagouv/gestion-des-subventions-locales) : Correction de vulnérabilités via la mise à jour des dépendances.
- [grist-core](/repos/betagouv/grist-core) : Correction de vulnérabilités.

## Autres changements notables
- **Infrastructure :** Migration vers Ruby 4.0 dans [turgot-metabase](/repos/betagouv/turgot-metabase) et vers Symfony 8 dans [mon-indemnisation-justice](/repos/betagouv/mon-indemnisation-justice).
- **Authentification :** Intégration de ProConnect dans [stage-direct](/repos/betagouv/stage-direct) et d'Ademe Connect dans [france-chaleur-urbaine](/repos/betagouv/france-chaleur-urbaine).
- **Refonte :** Refonte du formulaire de création de programme dans [mission-transition-ecologique-back](/repos/betagouv/mission-transition-ecologique-back) et de la landing page du simulateur dans [france-chaleur-urbaine](/repos/betagouv/france-chaleur-urbaine).
- **Données :** Mise à jour des données des aides vélo dans [publicodes-aides-velo](/repos/betagouv/publicodes-aides-velo) et des données des programmes dans [mission-transition-ecologique](/repos/betagouv/mission-transition-ecologique).
- **Déploiement :** Amélioration des processus de déploiement et de gestion des dépendances dans plusieurs dépôts (oauth2-deploy-demo, kube-dev, grist-utils).

## Dépôts les plus actifs
- [mon-service-securise](/repos/betagouv/mon-service-securise) : Refonte de l'interface, ajout de la gestion des administrateurs et amélioration de la sécurité.
- [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) : Amélioration de l'interface utilisateur, correction de bugs et ajout de nouvelles fonctionnalités.
- [mission-transition-ecologique](/repos/betagouv/mission-transition-ecologique) : Mise à jour des données et amélioration de l'interface.
- [infomedicament](/repos/betagouv/infomedicament) : Optimisation des performances et ajout de nouvelles fonctionnalités.
- [gestion-des-subventions-locales](/repos/betagouv/gestion-des-subventions-locales) : Ajout de filtres et amélioration de la gestion des documents.
- [france-chaleur-urbaine](/repos/betagouv/france-chaleur-urbaine) : Refonte du système de permissions et de la landing page.
- [sylvasan](/repos/betagouv/sylvasan) : Ajout de nouvelles fonctionnalités pour la gestion des enquêtes.
- [test-sme](/repos/betagouv/test-sme) : Amélioration de l'expérience utilisateur et maintenance technique.
- [maestro](/repos/betagouv/maestro) : Ajout d'une interface administrateur et amélioration de la gestion des prélèvements.
- [nitrates](/repos/betagouv/nitrates) : Ajout d'un éditeur YAML en ligne et amélioration de l'interface utilisateur.
