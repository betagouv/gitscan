# Synthèse d'activité : proconnect-gouv (du 01/09 au 02/09)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance des fonctionnalités d'authentification et une modernisation de l'architecture globale. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur (optimisation du MFA, intégration des Passkeys, interface mobile) et la robustesse des services d'identité.

Parallèlement, l'écosystème s'enrichit avec le lancement de nouveaux services de test et de résolution technique, ainsi qu'une refonte structurelle de plusieurs composants clés pour gagner en autonomie et en efficacité.

## Sécurité
- Renforcement de l'authentification via un assistant MFA et l'optimisation de l'usage des Passkeys dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite).
- Amélioration de la sécurité de la fédération avec le blocage par défaut des domaines d'e-mails lors de la création d'un IdP et la réutilisation des sessions MFA pour fluidifier l'accès dans [federation](/repos/proconnect-gouv/federation).
- Correction de vulnérabilités de dépendances dans [class-validator](/repos/proconnect-gouv/class-validator).

## Autres changements notables
- **Évolutions architecturales majeures** : Migration vers un nouveau modèle de "connectors" et passage à une synchronisation directe des données SIREN dans [proconnect-identite](/repos/proconnect-gouv/proconnect-identite). Simplification des serveurs de ressources et transformation de `csmr-rie` en application autonome dans [federation](/repos/proconnect-gouv/federation).
- **Infrastructure et support** : Extension du support matériel pour l'architecture `arm64` dans [api-partenaires](/repos/proconnect-gouv/api-partenaires).
- **Lancements de nouveaux projets** : Initialisation de [proconnect-test-idp](/repos/proconnect-gouv/proconnect-test-idp) (fournisseur d'identité de test), [mx-resolver](/repos/proconnect-gouv/mx-resolver) (résolution DNS) et [bun-buildpack](/repos/proconnect-gouv/bun-buildpack) (déploiement Scalingo).

## Dépôts les plus actifs
- [proconnect-identite](/repos/proconnect-gouv/proconnect-identite) : Évolutions majeures sur l'architecture, la sécurité et la gestion des données.
- [federation](/repos/proconnect-gouv/federation) : Améliorations significatives de la sécurité, de l'expérience utilisateur et de la structure logicielle.
- [proconnect-espace-partenaires](/repos/proconnect-gouv/proconnect-espace-partenaires) : Optimisation de l'interface mobile, du processus de connexion et de la documentation.
- [class-validator](/repos/proconnect-gouv/class-validator) : Enrichissement de la bibliothèque avec de nouveaux validateurs et correctifs de sécurité.
