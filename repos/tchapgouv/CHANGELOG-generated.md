# Synthèse d'activité : tchapgouv (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation tchapgouv s'est concentrée sur l'amélioration de la sécurité, de la stabilité et de l'expérience utilisateur de ses applications. Des efforts importants ont été déployés pour renforcer la sécurité des communications en désactivant les salons privés non chiffrés et en ajustant les options de connexion. Des améliorations significatives ont également été apportées aux infrastructures de CI/CD, à la gestion des dépendances et à la documentation, visant à faciliter le développement et le déploiement des applications. Les applications web et mobiles (Tchap Desktop, Tchap iOS, Tchap Android) ont bénéficié de corrections de bugs et d'optimisations diverses.

## Sécurité
Plusieurs dépôts ont reçu des mises à jour axées sur la sécurité :

- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Suppression de la création de comptes hérités sans passer par le MAS, renforçant ainsi la sécurité et la conformité du processus d'authentification.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Désactivation des salons privés non chiffrés pour une meilleure protection des conversations.

## Autres changements notables
- [element-call](/repos/tchapgouv/element-call) : Renommage du projet en "element-call-tchap" et correction d'un problème de compatibilité sur Firefox avec les appareils utilisant un proxy.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Ajout de la possibilité de créer des salons privés non chiffrés (désactivés par défaut sur iOS) et ouverture des appels groupés pour certains environnements.
- [synapse](/repos/tchapgouv/synapse) : Activation de l'expiration des comptes via MAS et mise en cache de l'introspection MAS pour améliorer les performances.
- [matrix-spec](/repos/tchapgouv/matrix-spec) : Ajout de la spécification pour le support de la méthode d'autorisation d'appareil (Device Authorization Grant).

## Dépôts les plus actifs
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Nombreuses corrections de bugs, améliorations de l'interface utilisateur et mises à jour de dépendances.
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Améliorations de la sécurité, corrections de bugs et refactorisation du code.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Ajout de nouvelles fonctionnalités, corrections de bugs et mises à jour du SDK Matrix Rust.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Améliorations des tests d'authentification et refactorisation du code.
- [compound-web](/repos/tchapgouv/compound-web) : Améliorations techniques liées à l'infrastructure CI/CD et à la gestion des dépendances, ainsi qu'une amélioration visuelle des boutons.
