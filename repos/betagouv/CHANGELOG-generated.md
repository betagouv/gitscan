# Synthèse d'activité : betagouv (du 17/05 au 17/07)

## Résumé de l'activité
L'activité récente de l'organisation betagouv a été marquée par des améliorations significatives en matière de sécurité, de performance et d'expérience utilisateur sur de nombreux projets. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités et renforcer la sécurité. Des efforts importants ont été déployés pour améliorer l'intégration des données entre différents services, notamment avec l'ajout de synchronisations entre Turgot et Matomo, et l'intégration de nouvelles sources de données pour des projets comme *ma-cantine*.  De nombreux projets ont également vu des améliorations de l'interface utilisateur, des corrections de bugs et des optimisations de la performance. Les projets *sylvasan*, *mission-transition-ecologique* et *mon-aide-cyber* ont connu des évolutions notables en termes de fonctionnalités et de stabilité.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :

*   Correction d'une vulnérabilité XSS dans [mon-service-securise-journal](/repos/betagouv/mon-service-securise-journal).
*   Mise à jour de dépendances vulnérables dans [mon-profil-anssi](/repos/betagouv/mon-profil-anssi).
*   Implémentation de TLS et d'une authentification par certificat dans [lab-anssi-antivirus](/repos/betagouv/lab-anssi-antivirus).
*   Ajout de `checkov` et `zizmor` pour la validation de la configuration dans [lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit).
*   Vérification du certificat MQC dans [lab-anssi-admin](/repos/betagouv/lab-anssi-admin).

## Autres changements notables
*   **Refonte d'architecture:** Refonte de l'architecture de l'API dans [signalement-api](/repos/betagouv/signalement-api) et refactorisation du code dans [sylvasan](/repos/betagouv/sylvasan).
*   **Intégration de données:** Ajout de nouvelles sources de données dans [ma-cantine](/repos/betagouv/ma-cantine) et [mle-back](/repos/betagouv/mle-back).
*   **CI/CD:** Amélioration des workflows CI/CD dans plusieurs dépôts, notamment [mission-transition-ecologique-back](/repos/betagouv/mission-transition-ecologique-back) et [matomo-to-pg](/repos/betagouv/matomo-to-pg).
*   **Migration de technologies:** Passage à pnpm dans [test-sme](/repos/betagouv/test-sme) et migration vers Node.js dans [sante-psy](/repos/betagouv/sante-psy).
*   **Nouvelles fonctionnalités:** Ajout de la fonctionnalité de duplication d'enquêtes dans [sylvasan](/repos/betagouv/sylvasan) et de la gestion des risques dans [mon-service-securise](/repos/betagouv/mon-service-securise).

## Dépôts les plus actifs
*   [sylvasan](/repos/betagouv/sylvasan) : Amélioration significative de l'application mobile et web, ajout de nouvelles fonctionnalités et corrections de bugs.
*   [mission-transition-ecologique](/repos/betagouv/mission-transition-ecologique) : Amélioration de l'interface utilisateur et de la gestion des données.
*   [mon-service-securise](/repos/betagouv/mon-service-securise) : Amélioration de la gestion des risques et renforcement de la sécurité.
*   [ma-cantine](/repos/betagouv/ma-cantine) : Intégration de nouvelles sources de données et amélioration de l'interface utilisateur.
*   [lab-anssi-ui-kit](/repos/betagouv/lab-anssi-ui-kit) : Amélioration de plusieurs composants et renforcement de la sécurité du CI.
*   [mon-aide-cyber](/repos/betagouv/mon-aide-cyber) : Amélioration de la sécurité et corrections de bugs.
*   [test-sme](/repos/betagouv/test-sme) : Amélioration de l'expérience utilisateur et maintenance technique.
*   [transports-sanitaires](/repos/betagouv/transports-sanitaires) : Refonte majeure du simulateur de transport sanitaire.
*   [nitrates](/repos/betagouv/nitrates) : Amélioration de l'interface administrateur et de la gestion des données.
*   [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) : Refonte des formulaires d'inscription et amélioration du partage de missions.
