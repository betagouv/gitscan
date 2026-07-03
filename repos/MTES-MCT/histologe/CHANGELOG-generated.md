## Changelog : histologe (30 derniers jours, au 01 Juillet 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'expérience utilisateur, notamment au niveau du formulaire de suivi usager avec des corrections d'accessibilité et des améliorations de l'interface. Des corrections de bugs et des optimisations techniques ont également été apportées, ainsi que des évolutions concernant la gestion des signalements et des données, notamment l'ajout de fonctionnalités pour les injonctions aux bailleurs et la gestion des doublons.

### Évolutions fonctionnelles

*   **Formulaire de suivi usager :** Amélioration de l'accessibilité avec des validations W3C, harmonisation des boutons et déplacement de l'encart sur le dossier [#5996].
*   **Démarche Accélérée :** Affinements du système de relances [#6053] et ajout d'un mini-dashboard [#5942].
*   **Espace bailleur :** Améliorations rapides et modification du champ d'upload de fichier [#6023, #5940].
*   **Gestion des signalements :**
    *   Ajout d'un filtre "Démarche accélérée" dans la liste des signalements [#6041].
    *   Commande temporaire de clôture de signalements en back-office [#6040].
    *   Possibilité de clôturer des signalements à partir d'un fichier CSV [#6020].
*   **RT (Réseau de Terrain) :** Création d'une liste des doublons de dossiers à la même adresse [#5864].
*   **Annuaire :** Correction de l'export pour les utilisateurs non-RT [#5925].
*   **Injonction bailleur :** Améliorations et suppression du résumé des suivis générés par l'IA [#6023, #6039].
*   **Ajout d'une colonne "zones"** à l'export des données [#5883].
*   **Ajout d'insalubrité** lorsque l'absence d'eau chaude est signalée [#5908].

### Évolutions techniques

*   **Rationalisation des flush :** Première étape d'une optimisation de la gestion des flush en base de données [#5977].
*   **Nettoyage de la table signalement :** Optimisation de la table signalement [#5950].
*   **Mise à jour de Jmespath :** Correction d'une vulnérabilité de sécurité (CVE) [#6028].
*   **Mise à jour des dépendances :**
    *   Mise à jour de npm packages [#6036, #5964, #5965].
    *   Mise à jour de tinymce [#5955].
*   **Configuration CI/CD :** Utilisation de `.env.ci` dans le pipeline CI principal [#5842].
*   **Sentry Monitoring :** Exclusion des messages provenant du scheduler (esabora) des alertes Sentry [#5978].
*   **Suppression d'une variable d'environnement :** Suppression de `FEATURE_INJONCTION_BAILLEUR` [#6000].

### Autres changements

*   **Documentation API :** Mise à jour de la documentation de l'API [#5928].
*   **Commandes de gestion :** Ajout de nouvelles commandes pour la gestion des données (mise à jour des communes fusionnées, désynchronisation Sish) [#5910, #6019].
*   **Amélioration de la navigation au clavier :** Amélioration de l'accessibilité du formulaire Pro [#6005].
*   **Corrections de bugs :** Diverses corrections de bugs mineurs et améliorations de la stabilité [#6016, #6017, #6052, #6055, #6062, #5954, #5959, #5970, #5971, #5972, #5981].
*   **Corrections de pagination :** Correction d'un bug lié à la pagination de l'API Permissions [#6075].
*   **Correction d'un TypeError :** Correction d'une erreur de type lors de la normalisation du code INSEE [#6055].
*   **Gestion des erreurs d'envoi Brevo :** Amélioration du suivi des erreurs d'envoi d'emails Brevo [#5952].
