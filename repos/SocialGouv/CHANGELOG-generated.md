# Synthèse d'activité : SocialGouv (du 15 mai au 15 juin 2026)

## Résumé de l'activité
L'activité récente de SocialGouv a été marquée par une forte concentration sur l'amélioration de la sécurité, la modernisation des infrastructures et l'enrichissement des fonctionnalités de ses outils. Plusieurs dépôts ont bénéficié de migrations vers des gestionnaires de paquets plus performants comme pnpm, renforçant ainsi la sécurité et la gestion des dépendances. Des efforts importants ont également été déployés pour améliorer l'accessibilité des services, notamment via l'intégration de nouvelles fonctionnalités et la correction de bugs. L'organisation prépare activement l'arrêt de certains services, tout en continuant à développer de nouveaux outils et à améliorer l'expérience utilisateur de ses plateformes existantes. Les dépôts [vao](/repos/SocialGouv/vao), [token-bureau](/repos/SocialGouv/token-bureau), [srdt](/repos/SocialGouv/srdt), [smart-allow](/repos/SocialGouv/smart-allow), [legi-data](/repos/SocialGouv/legi-data) et [cdtn-admin](/repos/SocialGouv/cdtn-admin) ont été particulièrement actifs.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations significatives en matière de sécurité. [smart-allow](/repos/SocialGouv/smart-allow) a ajouté une fonctionnalité bloquant l'envoi de données à des fournisseurs d'IA externes, et [dsfr-mcp](/repos/SocialGouv/dsfr-mcp) a reçu une correction de sécurité importante. [domifa](/repos/SocialGouv/domifa) a également bénéficié de corrections de vulnérabilités. [buildkit-operator](/repos/SocialGouv/buildkit-operator) a renforcé la sécurité de la chaîne d'approvisionnement logicielle avec l'implémentation de la signature cosign et de la génération de SBOM.

## Autres changements notables
Plusieurs dépôts ont connu des évolutions techniques majeures. [vao](/repos/SocialGouv/vao) a migré vers des routes Typescript et augmenté les ressources de sa base de données. [token-bureau](/repos/SocialGouv/token-bureau) a refactorisé son code en un monorepo et migré vers pnpm. [matomo-postgres](/repos/SocialGouv/matomo-postgres) a mis à jour sa version de Node.js. [infra-apps](/repos/SocialGouv/infra-apps) a migré les datastores d'Iterion vers une infrastructure plus robuste. [cdtn-admin](/repos/SocialGouv/cdtn-admin) a ajouté un script pour le dump de la base de données.

## Dépôts les plus actifs
*   [vao](/repos/SocialGouv/vao) : Amélioration de l'expérience utilisateur pour le renouvellement d'agrément et implémentation de la validation OTP.
*   [token-bureau](/repos/SocialGouv/token-bureau) : Corrections de bugs, améliorations de la gestion des permissions et migration vers pnpm.
*   [srdt](/repos/SocialGouv/srdt) : Améliorations de l'expérience utilisateur, de l'accessibilité et ajout de nouvelles fonctionnalités.
*   [cdtn-admin](/repos/SocialGouv/cdtn-admin) : Ajout de nouveaux types de contributions et amélioration de la gestion des données.
*   [matomo-next](/repos/SocialGouv/matomo-next) : Ajout d'un proxy de suivi côté serveur et prise en charge des tests A/B.
*   [dashlord](/repos/SocialGouv/dashlord) : Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités de gestion des données.
*   [legi-data](/repos/SocialGouv/legi-data) : Mises à jour régulières des données législatives.
*   [iterion](/repos/SocialGouv/iterion) : Activation de l'inscription ouverte et déploiement d'une marketplace de bots.
