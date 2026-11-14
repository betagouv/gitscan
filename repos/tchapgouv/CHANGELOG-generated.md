# Synthèse d'activité : tchapgouv (du 01/03 au 31/10)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur l'amélioration de l'expérience utilisateur et la robustesse de l'infrastructure. Les applications mobiles bénéficient de fonctionnalités majeures comme la gestion du multi-compte et des notifications enrichies sur [tchap-x-android](/repos/tchapgouv/tchap-x-android), tandis que [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) profite d'une interface simplifiée et d'une base de code modernisée. Sur le web, [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) introduit un lecteur Markdown pour les pièces jointes, améliorant la lecture des documents partagés.

Côté infrastructure, des efforts importants ont été déployés pour accroître la performance et la sécurité des services. L'optimisation des processus de routage dans [simple-border-gateway](/repos/tchapgouv/simple-border-gateway) et l'intégration de Rust dans [synapse](/repos/tchapgouv/synapse) visent à garantir une plateforme plus fluide et capable de supporter une charge accrue.

## Sécurité
- Activation par défaut de la vérification des appareils sur [tchap-web-v4](/repos/tchapgouv/tchap-web-v4).
- Renforcement de la sécurité des certificats sur [tchap-ios](/repos/tchapgouv/tchap-ios) et [tchap-android](/repos/tchapgouv/tchap-android) (certification Harica et compatibilité F-Droid).
- Corrections critiques de sécurité dans [synapse](/repos/tchapgouv/synapse) contre la traversée de chemin et l'usurpation d'identité.
- Sécurisation du processus d'authentification via [matrix-authentication-service-tchap](/repos/tchapgouv/matrix-authentication-service-tchap) en supprimant la création de comptes hors service officiel.
- Amélioration de la gestion des erreurs et de la sécurité HTTP dans [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) et [simple-border-gateway](/repos/tchapgouv/simple-border-gateway).
- Suppression d'un token npm dans le workflow CI/CD de [element-call](/repos/tchapgouv/element-call) pour renforcer la sécurité.

## Autres changements notables
- Optimisation majeure de la réactivité de [tchap-x-android](/repos/tchapgouv/tchap-x-android) par le déportement des tâches lourdes (base de données, médias) hors du thread principal.
- Amélioration significative des performances de [synapse](/repos/tchapgouv/synapse) grâce à l'utilisation de Rust pour la sérialisation et l'accès aux données.
- Modernisation de la base de code de [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) via un rebase majeur sur ElementX-iOS.
- Mise en place d'un système de limitation de débit (rate limiting) par utilisateur dans [matrix-media-repo](/repos/tchapgouv/matrix-media-repo).
- Refonte du framework de commande de [matrix-admin-bot](/repos/tchapgouv/matrix-admin-bot) pour une meilleure gestion des opérations complexes via des verrous et des étapes.
- Optimisation du routage dans [simple-border-gateway](/repos/tchapgouv/simple-border-gateway) par le remplacement des expressions régulières par `matchit`.

## Dépôts les plus actifs
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Déploiement de nouvelles fonctionnalités de messagerie et de gestion multi-compte.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Épuration de l'interface utilisateur et mise à jour technique majeure.
- [synapse](/repos/tchapgouv/synapse) : Évolutions majeures sur la gestion des utilisateurs, la sécurité et les performances.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de l'expérience de connexion et de la gestion des comptes.
- [simple-border-gateway](/repos/tchapgouv/simple-border-gateway) : Optimisations de routage et renforcement de la robustesse de la configuration.
