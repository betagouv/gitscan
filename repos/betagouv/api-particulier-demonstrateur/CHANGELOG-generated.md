## Changelog : api-particulier-demonstrateur (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur et de la clarté de l'interface. L'accent a été mis sur l'optimisation des parcours "Cantine" et "Transport", notamment pour mieux guider les utilisateurs lors des étapes d'authentification FranceConnect et de téléchargement de documents.

### Évolutions fonctionnelles
- **Parcours Cantine** :
    - Ajout d'un message d'information sur la récupération automatique des justificatifs avant l'étape FranceConnect [#6944](https://github.com/betagouv/api-particulier-demonstrateur/issues/6944).
    - Amélioration de l'interface de connexion : ajustement des espacements et correction de l'affichage des alertes pour éviter qu'elles ne soient masquées par le pied de page.
    - Correction d'une coquille (espace superflu) dans le texte d'aide au téléchargement.
- **Parcours Transport** :
    - Déplacement du panneau d'information FranceConnect de la section éligibilité vers la section connexion pour une meilleure cohérence de parcours.
    - Ajustement de la largeur de la boîte d'aide COG pour un meilleur rendu visuel dans ses colonnes.
- **Authentification** :
    - Masquage du panneau d'information FranceConnect pour les profils utilisateurs n'utilisant pas ce mode d'authentification.

### Évolutions techniques
- **Infrastructure & CI** : Mise à jour de la chaîne de CI pour l'exécution sous Node 24 avec `npm ci`.
- **Routage** : Correction de la logique de résolution des cas d'usage basée sur les segments de l'URL (pathname).

### Autres changements
- **Qualité du code** : Mise à jour de la configuration Prettier (version 3.9) et reformatage de certains layouts.
- **Maintenance** : Optimisation de la gestion des dépendances via la configuration de mises à jour hebdomadaires et le verrouillage des versions majeures pour Dependabot.
