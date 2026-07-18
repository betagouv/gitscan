## Changelog : tchap-x-ios (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'expérience utilisateur, notamment concernant la création de salles privées chiffrées et la gestion des mentions. Des corrections ont également été apportées pour améliorer la stabilité et la compatibilité de l'application, ainsi que des mises à jour de sécurité avec le renouvellement des certificats.

### Évolutions fonctionnelles
- Ajout d'un badge suggéré lors de la création d'une salle privée chiffrée.
- Réactivation du flux d'enregistrement MAS.
- Correction de la couleur des mentions "autres" pour une meilleure lisibilité en mode sombre.
- Suppression de l'effet de verre sur l'en-tête des salles.
- Modification du nom de l'application dans certains écrans et permissions pour refléter la marque Tchap.
- Conversion de l'identifiant utilisateur de l'application classique au format email.

### Évolutions techniques
- Mise à jour du SDK Rust Matrix.
- Mise à jour de la librairie `compound-design-tokens` (version 10.2.1).
- Remplacement des certificats Let's Encrypt expirés en pré-production et ajout d'un nouveau certificat Harica en production.
- Suppression de la fonctionnalité expérimentale pour les salles privées non chiffrées.
- Désactivation de l'abonnement aux threads qui causait une boucle de tentatives infinies.
- Renommage de l'environnement "staging" en "preprod".
- Suppression du "X" dans les noms de certains environnements.

### Autres changements
- Correction de typos et amélioration de la formulation dans l'application.
- Restrictions sur l'écran des espaces pour éviter les vues vides.
- Montée de version de l'application.
- Correction de problèmes de build Xcode après un rebase.
