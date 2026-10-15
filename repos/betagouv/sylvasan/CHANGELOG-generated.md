## Changelog : sylvasan (30 derniers jours, au 14 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience de terrain via l'application mobile (cartographie, boussole, gestion des photos) et le renforcement de la sécurité de la plateforme. L'administration a également bénéficié de nouveaux outils de gestion des images et d'une meilleure granularité des permissions.

### Évolutions fonctionnelles
- **Cartographie et Mobile** :
    - Ajout d'une boussole et support de l'orthophoto sur le terrain.
    - Amélioration de la réactivité de la carte (gestion du zoom et affichage lors du retour au premier plan).
    - Possibilité de prendre des photos directement via l'appareil photo du téléphone.
- **Saisie de données et Formulaires** :
    - Support des listes d'objets imbriqués (jusqu'à 2 niveaux) et affichage complet des labels et sous-champs dans les résumés.
    - Ajout de valeurs par défaut pour les champs de type texte et numérique.
    - Mise en place de la validation des dates.
- **Administration et Gestion** :
    - Les administrateurs de pôle peuvent désormais consulter les réponses liées à leur périmètre.
    - Création d'une API dédiée à la gestion des images pour les administrateurs.
    - Renommage des référentiels dans la console d'administration pour plus de clarté.
- **Expérience Utilisateur** :
    - Identification mobile simplifiée (possibilité d'utiliser l'email ou le nom d'utilisateur).
    - Ajout du glisser-déposer pour réorganiser l'ordre des pages [#623](https://github.com/betagouv/sylvasan/pull/623).

### Évolutions techniques
- **Sécurité** :
    - Renforcement de la sécurité du frontend et du backend via l'ajout d'en-têtes de protection (CSP, HSTS, X-Frame-Options, X-Content-Type-Options) [#622](https://github.com/betagouv/sylvasan/pull/622).
    - Mise en place d'une authentification par clé API.
- **Performance et Optimisation** :
    - Accélération du changement de style de carte.
    - Refactorisation de la compression d'images et de la fonction de capture d'images pour plus de fiabilité.
- **Architecture et Cartographie** :
    - Migration vers un nouveau worker pour Maplibre et optimisation de la géolocalisation (suppression de la redondance entre Capacitor et Maplibre).
    - Intégration de Sentry pour le suivi des erreurs sur les applications web et mobiles.
    - Mise à jour de la version Android de l'application.

### Autres changements
- **Documentation** : Ajout d'un document d'architecture (ADR) expliquant les choix techniques concernant les référentiels.
- **Maintenance** : Mise à jour des outils de pré-validation du code (precommit).
