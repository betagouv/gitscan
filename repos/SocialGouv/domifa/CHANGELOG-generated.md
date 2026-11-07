## Changelog : domifa (30 derniers jours, au 06/11/2026)

### Résumé
Ce mois a été marqué par un renforcement significatif de la sécurité des données et une amélioration de l'expérience de gestion. Les principales évolutions concernent l'intégration systématique de scans antivirus sur les fichiers importés, le déploiement d'un "mode support" pour faciliter l'assistance technique sans risque de modification accidentelle, et la restauration de certaines capacités d'édition de profils pour les agents et les facteurs.

### Évolutions fonctionnelles
- **Gestion des usagers :**
    - Restauration de la possibilité pour les agents et les facteurs de modifier les coordonnées (téléphone et email) des usagers.
    - Amélioration de la précision des résultats de recherche pour les usagers ([#4341](https://github.com/SocialGouv/domifa/pull/4341)).
    - Mise en place d'une synchronisation automatique de la liste des usagers avec le serveur lors du retour sur l'onglet.
- **Interface et navigation :**
    - Ajout de menus déroulants de sélection de portail sur les pages de connexion (Admin, Stats, Usagers).
    - Amélioration de la navigation dans les pages d'historique et mise à jour des onglets.
    - Ajout d'un avis de maintenance programmé pour le 19 novembre sur les différents portails.
- **Formulaires :**
    - Normalisation automatique des noms et prénoms lors de la saisie.
    - Affichage explicite des erreurs de scan antivirus sur le formulaire de contact.

### Évolutions techniques
- **Sécurité et Antivirus :**
    - Intégration de ClamAV pour le scan systématique des fichiers lors de l'import d'usagers, des pièces jointes du support et des formulaires de contact.
    - Renforcement de la validation des types de fichiers avant scan et gestion robuste des erreurs de téléchargement.
    - Amélioration de la politique de sécurité du contenu (CSP) via le bundling des configurations DSFR.
- **Mode Support :**
    - Implémentation d'un mode support complet permettant de consulter l'interface en lecture seule (désactivation des formulaires, des boutons d'export et de saisie) pour sécuriser les sessions d'assistance.
- **Architecture et Données :**
    - Migration des identifiants des ayants droit vers le format UUID v7 pour une meilleure sécurité et performance.
    - Durcissement des endpoints API (usagers) et optimisation du parsing des identifiants (integers).
    - Optimisation de la logique de synchronisation (`lastSync`) pour garantir l'intégrité des données entre le client et le serveur.
- **Infrastructure et CI/CD :**
    - Mise à jour de l'environnement vers Node.js 24.
    - Optimisation des images de runtime et des pipelines GitLab CI/CD.

### Autres changements
- **Écosystème :** Création d'un "marketplace" de plugins DomiFa pour le partage de compétences de sécurité.
- **Contenu :** Mise à jour des éléments de la fenêtre contextuelle des actualités (news popup).
