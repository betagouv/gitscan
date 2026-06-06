# Synthèse d'activité : proconnect-gouv (du 28 avril 2026 au 04 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation proconnect-gouv s'est concentrée sur l'amélioration de la sécurité, la correction de bugs et l'ajout de nouvelles fonctionnalités, notamment autour de l'identité et de l'authentification. Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour renforcer la sécurité et la stabilité. Des améliorations significatives ont été apportées à [proconnect-identite] pour simplifier l'inscription des petites organisations, améliorer les messages d'erreur OIDC et gérer les rejets de modération.  [hyyypertool] a également connu des évolutions notables avec l'ajout de motifs de refus pour les utilisateurs et l'amélioration de l'interface utilisateur.

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de dépendances pour corriger des vulnérabilités. [class-validator] a notamment mis à jour ses dépendances pour améliorer la sécurité. [federation] a renforcé la sécurité de la validation d'email en utilisant DNS-over-HTTPS.

## Autres changements notables
- Migration de la base de données MongoDB de [proconnect-espace-partenaires] vers `corev2`.
- Publication du package `rne` par [proconnect-identite] pour une utilisation publique.
- Mise à jour de Node vers la version 24.16 dans [federation].
- Implémentation d'une limitation de débit basée sur l'adresse IP dans [hyyypertool].
- Création d'un client dédié pour l'environnement de pré-production dans [proconnect-identite].

## Dépôts les plus actifs
- [proconnect-identite] : Améliorations majeures de l'expérience utilisateur et de la gestion des identités, incluant la simplification de l'inscription et l'amélioration des messages d'erreur.
- [hyyypertool] : Ajout de fonctionnalités pour la gestion des utilisateurs et des modérations, ainsi que des améliorations de l'interface utilisateur.
- [class-validator] : Ajout de nouveaux validateurs et amélioration de la validation des données.
- [federation] : Améliorations de l'API et de la sécurité, notamment avec l'utilisation de DNS-over-HTTPS.
- [proconnect-test-client] : Amélioration de la gestion de l'authentification multi-facteurs (MFA).
