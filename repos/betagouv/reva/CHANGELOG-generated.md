## Changelog : reva (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'intégration FranceConnect, avec une gestion plus robuste des données utilisateurs et une expérience utilisateur optimisée. Des corrections et des évolutions ont également été apportées à l'administration des certifications, notamment pour les comptes locaux, ainsi qu'à la gestion des cohortes VAE collectives. Enfin, des efforts ont été consentis pour améliorer la documentation et la qualité du code.

### Évolutions fonctionnelles
- Amélioration de l'intégration FranceConnect : ajout de champs optionnels (numéro de téléphone, localité, code postal, adresse) et gestion des erreurs améliorée. (#19)
- Ajout d'une page d'erreur plus informative lors de l'authentification avec FranceConnect. (#19)
- Possibilité de se déconnecter via Keycloak pour les utilisateurs authentifiés avec FranceConnect. (#19)
- Amélioration de l'affichage des informations sur les certifications dans l'interface d'administration. (#35, #36)
- Ajout d'une confirmation lors de la sélection d'une certification non disponible pour une cohorte VAE collective. (#20)
- Affichage d'un indicateur visuel pour les certifications en mode lecture seule dans l'administration. (#20)
- Correction de l'affichage du coût du jury dans l'administration et sur le site web. (#12)
- Ajout d'un message d'information sur FranceConnect sur les pages de connexion et d'inscription. (#19)
- Amélioration de la gestion des adresses candidates, permettant de gérer le cas où le candidat n'est pas né en France. (#5)

### Évolutions techniques
- Refactorisation de la gestion des callbacks FranceConnect et amélioration de la sécurité avec l'utilisation de JWT. (#19)
- Mise à jour des dépendances (Next.js, React, Fastify) dans plusieurs packages. (#20, #21, #22)
- Ajout de tests Playwright pour l'administration des certifications des comptes locaux. (#1)
- Ajout de tests unitaires pour certaines fonctions API. (#20)
- Ajout d'une table `parcours_certification` et d'un resolver GraphQL associé. (#6)
- Ajout d'un champ `franceConnectLinked` au modèle `Candidate`. (#19)
- Suppression de la table `CandidateInfoFranceConnect` et intégration des informations dans le modèle `Candidate`. (#19)
- Ajout d'un champ `inseeCode` au modèle `Country`. (#19)
- Ajout d'un schéma d'architecture applicative. (#7)
- Refactorisation du code pour simplifier la logique de layout et utiliser de nouveaux composants (Panel). (#8)

### Autres changements
- Ajout de documentation. (#7)
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des configurations et des fichiers `.gitignore`.
- Génération des package locks. (#20)
- Ajout d'une configuration Metabase pour un nouveau dashboard. (#10)
- Correction d'un problème d'envoi d'emails pour les décisions d'éligibilité. (#9)
