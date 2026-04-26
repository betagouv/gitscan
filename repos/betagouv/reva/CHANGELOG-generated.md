## Changelog : reva (30 derniers jours, au 2026-04-24)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans les formulaires et la gestion des candidatures, avec un accent particulier sur l'intégration de FranceConnect. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des évolutions techniques pour faciliter la maintenance et l'évolutivité du projet.

### Évolutions fonctionnelles
- **FranceConnect :** Amélioration du flux d'abonnement AAP avec un avertissement concernant l'email et le SIRET. Correction d'un bug empêchant la planification d'une date de jury antérieure à la date d'envoi du dossier de validation.
- **Gestion des candidatures :** Possibilité de modifier la ville et le département de naissance pour les candidats FranceConnect. Correction d'un bug lié à la sélection de villes non uniques dans le composant d'autocomplétion d'adresse.
- **Interface Admin :**
    - Affichage par défaut des accordéons pour les autorités de certification si le résultat de la faisabilité n'est ni admissible ni rejeté.
    - Alignement de la carte blanche admin avec la largeur du conteneur DSFR.
    - Alignement de la page d'informations générales du compte local avec les spécifications Figma.
    - Affichage de l'autorité de certification sur la page d'informations générales du compte local.
    - Alignement des champs de contact du compte local.
    - Ajout d'une page de nettoyage des candidats FranceConnect en sandbox.
    - Ajout d'une page pour gérer les décisions de jury par blocs.
    - Amélioration de la page de signalement des problèmes de DV.
    - Possibilité de limiter le nombre d'heures de formation à 100.
    - Ajout d'une modale pour afficher les blocs inclus et non inclus dans la faisabilité.
- **VAE Collective :** Correction d'un bug lié aux tokens stockés dans les cookies.
- **Notifications :** Amélioration des messages d'erreur liés à FranceConnect.
- **Formulaires :** Amélioration du wording des champs requis (genre).
- **Expérience utilisateur :** Amélioration de la gestion des dates de décision de faisabilité (COMPLETE/INCOMPLETE).

### Évolutions techniques
- **API :**
    - Suppression de la logique d'attribution du rôle candidat lors du callback FranceConnect.
    - Refactorisation de la gestion des erreurs FranceConnect et ajout de logs pour faciliter le débogage.
    - Ajout d'index sur les tables de la base de données pour optimiser les requêtes.
    - Suppression de la fonctionnalité de connexion par lien magique.
    - Suppression des fonctionnalités liées à l'inscription candidat.
    - Ajout de la possibilité de révoquer une décision de jury.
    - Amélioration de la gestion des données DFF.
    - Ajout de la gestion des prénoms dans l'API.
- **Infrastructure :** Mise à jour de plusieurs dépendances (Fastify, Axios, Lodash, etc.).
- **Tests :** Ajout et mise à jour de nombreux tests unitaires et d'intégration.
- **Refactoring :** Réorganisation des dossiers de routes dans l'admin.
- **Sécurité :** Correction de vulnérabilités potentielles liées à la vérification des JWT et à l'utilisation de FranceConnect.
- **Suppression de code obsolète :** Suppression de plusieurs fonctionnalités et dépendances obsolètes.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Configuration :** Mise à jour de la configuration de l'environnement de développement.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Corrections de style :** Correction de problèmes de style et de formatage du code.
- **Mise à jour des versions des paquets :** De nombreuses mises à jour de dépendances ont été effectuées pour corriger des vulnérabilités et améliorer la stabilité.
