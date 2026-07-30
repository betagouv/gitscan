## Changelog : nitrates (30 derniers jours, au 2026-07-28)

### Résumé
Cette version apporte des améliorations significatives à la sécurité, à l'expérience utilisateur et à l'administration du simulateur de réglementation nitrates. Les corrections de vulnérabilités sont prioritaires, suivies d'améliorations de l'interface utilisateur, notamment sur mobile, et d'optimisations pour les administrateurs du système. Des améliorations de la gestion des données et de l'infrastructure sous-jacente ont également été apportées.

### Évolutions fonctionnelles
- **Simulateur :**
    - Amélioration du parcours utilisateur avec correction de bugs liés au scroll et au rechargement des données.
    - Correction de l'affichage des dates et des périodes dans le calendrier dynamique et le récapitulatif.
    - Amélioration de la gestion des champs de cascade et des renvois entre les différents éléments du simulateur.
    - Possibilité de précharger les données des questions complémentaires (QC) pour une expérience plus fluide.
- **Interface utilisateur :**
    - Amélioration de l'accessibilité clavier et de l'expérience utilisateur globale du simulateur.
    - Adaptation de l'interface pour une meilleure expérience sur mobile, notamment avec un bandeau d'information plus lisible et un affichage optimisé du calendrier.
    - Ajout d'infobulles claires et concises pour expliquer les différentes options et réglementations.
    - Amélioration de la cartographie et de l'affichage des données géographiques.
- **Administration :**
    - Ajout d'un filtre rapide pour la recherche de textes conditionnés dans l'interface d'administration.
    - Amélioration de l'éditeur YAML pour faciliter la modification des textes conditionnés.
    - Ajout d'un lien d'accès rapide vers la validation des feuilles dans la barre de navigation.
    - Possibilité de filtrer les données de validation par région (Hauts-de-France).
    - Validation des choix dans les migrations pour éviter les erreurs.

### Évolutions techniques
- **Sécurité :**
    - Correction de plusieurs vulnérabilités de sécurité identifiées lors d'un pentest (F3, F4).
    - Mise à jour des dépendances pour corriger les vulnérabilités connues (high, critical, medium).
    - Renforcement de la sécurité de la page de connexion administrateur.
    - Désactivation par défaut de la connexion administrateur par mot de passe.
- **Infrastructure & CI/CD :**
    - Mise en place d'un pipeline CI/CD avec des garde-fous pour garantir la qualité du code et la stabilité des déploiements.
    - Amélioration des tests unitaires et d'intégration.
    - Migration de la gestion des données de référentiels vers une base de données native pour une meilleure performance et flexibilité.
    - Optimisation de la configuration du CI pour éviter les faux négatifs.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Suppression de code obsolète et de résidus de développement.

### Autres changements
- Mise à jour de la documentation.
- Simplification des libellés publics pour les vergers et les vignes.
- Amélioration des messages d'information et des textes d'aide.
- Correction de bugs mineurs et améliorations de la stabilité.
- Ajout de points PAR par région pour une meilleure précision des données.
- Amélioration de la gestion des arbres de données et des snapshots.
