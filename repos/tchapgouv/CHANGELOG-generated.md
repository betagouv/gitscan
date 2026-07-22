# Synthèse d'activité : tchapgouv (du 04/07 au 18/07/2026)

## Résumé de l'activité
L'activité récente de tchapgouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment sur les applications mobiles (Tchap X iOS et Android) et les services de base (Synapse). Des efforts importants ont été déployés pour faciliter l'intégration et le déploiement des différents composants, ainsi que pour améliorer l'expérience utilisateur, en particulier concernant la gestion des salles et des comptes. L'organisation a également continué à travailler sur la modernisation de l'infrastructure et des outils de développement.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) a renouvelé ses certificats Let's Encrypt et ajouté un nouveau certificat Harica.
- [tchap-android](/repos/tchapgouv/tchap-android) a corrigé un problème de fingerprint de certificat pour F-Droid et mis à jour les certificats de juillet 2026.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) a mis à jour des dépendances (rustls-webpki, opa-wasm, wasmtime) pour corriger des vulnérabilités.

## Autres changements notables
- **Synapse:** Amélioration de la gestion des comptes utilisateurs, notamment la réactivation correcte des profils.
- **tchap-web-v4:** Correction d'une régression concernant l'intégration de l'appel embarqué et suppression de fonctionnalités expérimentales.
- **tchap-desktop:** Ajout de la possibilité d'installer l'application dans le contexte utilisateur et d'effectuer des mises à jour automatiques.
- **matrix-authentication-service:** Refonte de la construction de la configuration et ajout de tests pour la réactivation silencieuse de compte.
- **matrix-admin-bot:** Ajout de commandes pour gérer les utilisateurs (informations, remplacement d'email et de nom d'affichage) et envoyer des notifications à tous les utilisateurs.

## Dépôts les plus actifs
- [tchap-x-ios](/repos/tchapgouv/tchap-x-ios) : Amélioration de l'expérience utilisateur, corrections de bugs et mises à jour de sécurité.
- [tchap-x-android](/repos/tchapgouv/tchap-x-android) : Corrections de compatibilité, amélioration de la connexion avec Tchap Classique et ajout de fonctionnalités.
- [tchap-web-v4](/repos/tchapgouv/tchap-web-v4) : Corrections de bugs, amélioration de la stabilité et de l'intégration avec les nouvelles versions d'Element Call.
- [synapse](/repos/tchapgouv/synapse) : Amélioration de la gestion des comptes utilisateurs et correction de bugs.
- [matrix-authentication-service](/repos/tchapgouv/matrix-authentication-service) : Amélioration de l'expérience administrateur, correction de bugs et mise à jour des dépendances.
