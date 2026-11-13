## Changelog : domifa (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois-ci, Domifa a franchi des étapes clés pour renforcer la gestion administrative et l'accessibilité. Les capacités de gestion des comptes pour les DREETS et DDETS ont été étendues, et une mise en conformité majeure avec les normes d'accessibilité (RGAA) a été réalisée. L'introduction d'un nouveau "mode support" permet désormais aux administrateurs d'assister les utilisateurs plus efficacement, tandis que la sécurité a été considérablement renforcée par l'intégration systématique d'un antivirus sur tous les fichiers importés.

### Évolutions fonctionnelles
- **Gestion administrative et comptes**
  - Extension des droits de la DGCS pour la gestion des comptes DREETS et DDETS de chaque région [#4346](https://github.com/SocialGouv/domifa/pull/4346).
  - Ouverture de l'enregistrement aux domaines `.gouv.fr` spécifiques (Guyane, DRIHL).
  - Amélioration de la gestion des droits : les agents et facteurs peuvent à nouveau modifier les coordonnées (téléphone, email) des usagers.
  - Optimisation du formulaire d'invitation DDETS (demande du département avant l'email).
- **Accessibilité (RGAA)**
  - Mise en conformité globale suite aux audits d'accessibilité : correction des labels de liens, des boutons de réinitialisation de formulaire et amélioration de la navigation.
- **Expérience utilisateur (UX)**
  - **Mode Support :** Introduction d'un mode dédié permettant d'assister les usagers en rendant les formulaires sensibles (SMS, paramètres) en lecture seule pour éviter les erreurs de manipulation [#4323](https://github.com/SocialGouv/domifa/pull/4323).
  - **Navigation :** Ajout d'un menu déroulant de sélection de portail sur les pages de connexion pour faciliter l'accès aux différents services.
  - **Information :** Mise en place d'un système d'avis de maintenance pour informer les utilisateurs des interruptions de service prévues.

### Évolutions techniques
- **Sécurité et protection des données**
  - **Antivirus :** Intégration systématique de ClamAV pour scanner tous les fichiers importés (fichiers usagers, pièces jointes du support de contact) avant traitement.
  - **Durcissement (Hardening) :** Renforcement de la sécurité des points de terminaison (endpoints) usagers et de la validation des données (limitation de la taille des fichiers et des champs texte).
  - **CSP :** Optimisation de la politique de sécurité du contenu (CSP) via le déplacement de la configuration DSFR dans un script groupé.
- **Infrastructure et Backend**
  - **Migration Node.js :** Passage à Node.js 24 sur l'ensemble des packages et de la chaîne CI/CD.
  - **Gestion des identifiants :** Migration vers l'utilisation d'UUID v7 pour les bénéficiaires afin d'améliorer la sécurité et la performance.
  - **Optimisation CI/CD :** Amélioration des images de runtime GitLab et des processus de rendu des bundles frontend.
  - **Données :** Normalisation des noms/prénoms et amélioration de la gestion des migrations de données.

### Autres changements
- **Documentation :** Mise à jour des déclarations d'accessibilité suite aux derniers audits.
- **Outils de développement :** Création d'un "marketplace" de plugins Domifa pour faciliter le partage de compétences liées à la sécurité.
