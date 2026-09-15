## Changelog : labonnealternance (30 derniers jours, au 14 septembre 2026)

### Résumé
Ce mois a été marqué par une optimisation majeure de la visibilité du site (SEO) et de l'expérience de recherche. L'ajout de la recherche par département/région, l'amélioration de l'interface mobile (PWA) et l'automatisation de l'indexation sur les moteurs de recherche permettent une meilleure découverte des offres. Parallèlement, la plateforme a gagné en stabilité grâce à une meilleure gestion des processus automatiques et des erreurs techniques.

### Évolutions fonctionnelles
- **Recherche & Navigation**
  - Ajout de la recherche par département et région dans le champ de localisation ([#5248](https://github.com/mission-apprentissage/labonnealternance/issues/5248), [#5461](https://github.com/mission-apprentissage/labonnealternance/issues/5461)).
  - Amélioration de la navigation sur les fiches détails et unification avec le nouveau moteur de recherche ([#5194](https://github.com/mission-apprentissage/labonnealternance/issues/5194), [#5212](https://github.com/mission-apprentissage/labonnealternance/issues/5212)).
  - Optimisation de l'expérience de recherche sur mobile (modale et suggestions clavier) ([#5219](https://github.com/mission-apprentissage/labonnealternance/issues/5219), [#5220](https://github.com/mission-apprentissage/labonnealternance/issues/5220)).
  - Correction de la restauration du contexte de recherche lors de la consultation des fiches détails ([#5340](https://github.com/mission-apprentissage/labonnealternance/issues/5340), [#5341](https://github.com/mission-apprentissage/labonnealternance/issues/5341)).

- **SEO & Visibilité**
  - Mise en place de l'automatisation de l'indexation via Google Indexing API et IndexNow pour les nouvelles offres ([#5293](https://github.com/mission-apprentissage/labonnealternance/issues/5293), [#5271](https://github.com/mission-apprentissage/labonnealternance/issues/5271)).
  - Intégration de données structurées (Schema.org) pour les organisations et les formations ([#5270](https://github.com/mission-apprentissage/labonnealternance/issues/5270)).
  - Ajout de balises canonical pour optimiser le référencement des pages détails ([#5280](https://github.com/mission-apprentissage/labonnealternance/issues/5280)).

- **Expérience Utilisateur & Contenu**
  - Rendu de l'application installable sur mobile via la technologie PWA ([#5221](https://github.com/mission-apprentissage/labonnealternance/issues/5221)).
  - Enrichissement des contenus : nouveaux guides (recruteur, rémunération) et ajout de partenaires (Apecita, Marqueur Numérique) ([#5128](https://github.com/mission-apprentissage/labonnealternance/issues/5128), [#5142](https://github.com/mission-apprentissage/labonnealternance/issues/5142), [#5161](https://github.com/mission-apprentissage/labonnealternance/issues/5161), [#5299](https://github.com/mission-apprentissage/labonnealternance/issues/5299)).
  - Affichage de nouvelles données : compteur d'alternants recrutés ([#5201](https://github.com/mission-apprentissage/labonnealternance/issues/5201)) et engagements handicap des recruteurs ([#5222](https://github.com/mission-apprentissage/labonnealternance/issues/5222)).

- **Corrections diverses**
  - Résolution de plusieurs boucles de redirection critiques sur l'espace pro et les pages candidats ([#5388](https://github.com/mission-apprentissage/labonnealternance/issues/5388), [#5383](https://github.com/mission-apprentissage/labonnealternance/issues/5383), [#5245](https://github.com/mission-apprentissage/labonnealternance/issues/5245)).
  - Corrections d'affichage (bordures de tableaux, débordements de formulaires, largeur des fiches) ([#5345](https://github.com/mission-apprentissage/labonnealternance/issues/5345), [#5303](https://github.com/mission-apprentissage/labonnealternance/issues/5303), [#5217](https://github.com/mission-apprentissage/labonnealternance/issues/5217)).

### Évolutions techniques
- **Infrastructure & CI/CD**
  - Mise à jour de l'environnement de développement (Node 26, GitHub Actions) ([#5335](https://github.com/mission-apprentissage/labonnealternance/issues/5335)).
  - Mise à jour des images Docker (Metabase) ([#5392](https://github.com/mission-apprentissage/labonnealternance/issues/5392)).
  - Introduction d'un budget de performance pour le temps de chargement initial en CI ([#5191](https://github.com/mission-apprentissage/labonnealternance/issues/5191)).

- **Performance & Optimisation**
  - Réduction de la taille du CSS utilisé (DSFR) pour alléger les pages ([#5179](https://github.com/mission-apprentissage/labonnealternance/issues/5179)).
  - Parallélisation du traitement des données pour améliorer la rapidité des liens de formation ([#5204](https://github.com/mission-apprentissage/labonnealternance/issues/5204)).
  - Nettoyage du code lié à l'ancien moteur de recherche ([#5183](https://github.com/mission-apprentissage/labonnealternance/issues/5183)).

- **Fiabilité du Backend**
  - Amélioration de la stabilité des services tiers (Mistral AI, MongoDB, Brevo) et gestion des erreurs transitoires ([#5206](https://github.com/mission-apprentissage/labonnealternance/issues/5206), [#5230](https://github.com/mission-apprentissage/labonnealternance/issues/5230), [#5307](https://github.com/mission-apprentissage/labonnealternance/issues/5307)).
  - Optimisation des tâches planifiées (cron jobs) pour l'importation des offres et l'analyse des recherches ([#5312](https://github.com/mission-apprentissage/labonnealternance/issues/5312), [#5174](https://github.com/mission-apprentissage/labonnealternance/issues/5174)).
  - Renforcement de la sécurité (prévention de la fuite de secrets vers les outils de monitoring) ([#5294](https://github.com/mission-apprentissage/labonnealternance/issues/5294), [#5301](https://github.com/mission-apprentissage/labonnealternance/issues/5301)).

### Autres changements
- Nettoyage de la documentation obsolète et correction des liens rompus ([#5213](https://github.com/mission-apprentissage/labonnealternance/issues/5213)).
- Suppression d'endpoints API et de fonctions de géocodage inutilisés ([#5193](https://github.com/mission-apprentissage/labonnealternance/issues/5193), [#5467](https://github.com/mission-apprentissage/labonnealternance/issues/5467)).
