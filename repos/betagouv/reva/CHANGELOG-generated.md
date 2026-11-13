## Changelog : reva (30 derniers jours, au 12 novembre 2026)

### Résumé
Ce mois-ci a été marqué par une refonte majeure du parcours de soumission du Dossier de Validation (DV) pour les candidats, offrant une expérience plus fluide et dédiée. L'interface d'administration a également été modernisée pour mieux accompagner les organismes de certification, tandis que des mesures importantes ont été prises pour renforcer l'anonymisation des données et la sécurité des échanges.

### Évolutions fonctionnelles

**Pour les candidats**
- **Refonte du Dossier de Validation (DV) :** Nouveau parcours de soumission avec des pages dédiées, un meilleur affichage des alertes et des blocs de ressources pour faciliter la saisie.
- **Amélioration de l'ergonomie mobile :** Optimisation de l'affichage et de la réactivité de l'ensemble des formulaires (coordonnées, typologie, accord collectif, etc.) sur smartphone.
- **Enrichissement des informations de certification :** Affichage plus clair des codes RNCP, des dates d'expiration et des niveaux de diplôme sur les pages de certification.
- **Optimisation de la saisie :** Amélioration du composant d'autocomplétion pour les adresses et des filtres de recherche d'organismes.
- **Nouveauté :** Possibilité de soumettre une demande d'aménagement spécifique directement lors du processus de soumission du dossier de validation.

**Pour les organismes et l'administration**
- **Modernisation de la gestion des dossiers :** Refonte complète de la vue "Dossier de Validation" pour les autorités de certification, incluant de nouveaux indicateurs visuels et des alertes de suivi (ex: avertissement si une date d'examen est prévue mais le dossier n'est pas soumis).
- **Gestion des certifications :** Ajout de nouveaux outils de gestion (fenêtres modales) pour ajouter ou supprimer des certifications de manière plus efficace.
- **Suivi financier :** Intégration de nouveaux champs de saisie pour le suivi des financements, notamment pour les prises en charge via Transitions Pro.
- **Tableaux de bord :** Amélioration de l'accès et de l'affichage des tableaux de bord Metabase pour les sous-comptes dans le cadre de la VAE collective.

### Évolutions techniques

**Architecture et API**
- **Refonte de la gestion des autorités :** Restructuration profonde de la base de données pour lier les comptes aux autorités de certification via une nouvelle table dédiée, améliorant la robustesse du système.
- **Logique de visibilité :** Optimisation des algorithmes de recherche pour que la visibilité des certifications soit directement liée à l'existence de parcours actifs et liés à une autorité.
- **Sécurité des fichiers :** Renforcement des contrôles lors de l'upload (limitation stricte de la taille et des formats de fichiers autorisés).
- **Gestion des accès :** Augmentation de la durée de validité des codes OTP par email (passant de 10 à 30 minutes) pour améliorer l'expérience utilisateur.

**Sécurité et Données**
- **Anonymisation renforcée :** Extension majeure du script d'anonymisation de la base de données pour couvrir un spectre plus large de données sensibles (financements, compétences, rendez-vous, informations de paiement, etc.).
- **Sécurisation Metabase :** Mise en place d'un proxy OAuth2 pour sécuriser l'accès aux outils de statistiques.

**Infrastructure**
- **Optimisation des ressources :** Augmentation de la mémoire allouée au conteneur PostgreSQL pour améliorer les performances.

### Autres changements
- Nettoyage du code et suppression de composants et d'exports inutilisés.
- Suppression de la fonctionnalité d'export des résultats de jury.
