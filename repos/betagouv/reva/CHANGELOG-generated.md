## Changelog : reva (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, le projet reva a franchi des étapes importantes dans l'automatisation du processus de faisabilité dématérialisée et le renforcement de la sécurité. Les utilisateurs bénéficieront d'une gestion plus fluide des autorités de certification et de nouveaux outils de sélection pour les administrateurs. En coulisses, une refonte majeure du système de gestion des droits garantit une protection accrue et plus précise des données.

### Évolutions fonctionnelles
- **Parcours Candidat** : 
    - Amélioration du processus de faisabilité dématérialisée avec l'ajout de nouveaux retours d'information (feedbacks) et de pages dédiées.
    - Simplification de la gestion des autorités de certification : possibilité de sélection multiple, ajout de pages d'avertissement et de nouveaux éléments d'interface pour faciliter la prise de contact.
    - Correction de bugs d'affichage et de cache lors de la sélection des autorités de certification.
- **Outils Administrateurs** : 
    - Modernisation des composants de sélection (Formacodes v2) et amélioration des filtres pour les appels à projets (AAP).
    - Amélioration de la visibilité des informations relatives aux organismes et aux certificats de France Compétences.
- **VAE Collective** : 
    - Mise en place de permissions granulaires permettant un contrôle précis des actions sur les cohortes (voir, modifier, supprimer).

### Évolutions techniques
- **Sécurité et Autorisation** : 
    - Refonte complète du moteur d'autorisation de l'API via l'introduction d'un nouveau système de gestion des politiques (`withPolicies`), centralisant et sécurisant l'accès à l'ensemble des ressources (candidatures, organismes, jury, etc.).
    - Mise en œuvre d'un nouveau modèle de rôles et de permissions pour les collectifs VAE.
- **Infrastructure et Déploiement** : 
    - Résolution d'un problème de timeout lors du démarrage des services sur Scalingo via l'ajustement de la configuration de l'hôte.
- **Qualité et Tests** : 
    - Augmentation significative de la couverture de tests sur l'API, l'interface d'administration et les flux d'interopérabilité.
    - Optimisation des workflows CI pour exécuter des suites de tests plus complètes.
- **Maintenance de sécurité** : 
    - Remédiation de plusieurs vulnérabilités de haute sévérité identifiées sur les dépendances.

### Autres changements
- Nettoyage du code (linting) et suppression de configurations et de paramètres inutilisés.
