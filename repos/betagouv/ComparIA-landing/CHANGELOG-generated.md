## Changelog : ComparIA-landing (30 derniers jours, au 19 août 2026)

### Résumé
Ce mois a marqué le passage d'un projet initial à une plateforme de présentation complète et structurée. La landing page dispose désormais de sections dédiées aux produits, aux actualités et aux jeux de données. Un effort majeur a été porté sur l'accessibilité, le référencement (SEO) et l'optimisation des performances, tout en mettant en place une infrastructure permettant un auto-hébergement facilité.

### Évolutions fonctionnelles
- **Nouvelles pages et contenus** : Création des pages d'accueil, de produits, d'actualités, de jeux de données, de la FAQ et du plan du site.
- **Enrichissement de l'information** : Mise à jour de la FAQ (confidentialité, classement, consommation énergétique, estimation GPU) et ajout des jalons 2026 à la chronologie.
- **Accessibilité et SEO** : Amélioration globale de l'accessibilité (niveaux de titres, textes alternatifs, liens d'évitement, balises de navigation) et optimisation du référencement (sitemap, balises SEO).
- **Interface utilisateur** : Ajustements visuels sur les cartes d'actualités, alignement des logos partenaires (DINUM, Culture, ALT-EDIC) et repositionnement de la newsletter.

### Évolutions techniques
- **Infrastructure et déploiement** : Ajout d'un Dockerfile et de charts Helm (incluant un Ingress optionnel) pour faciliter l'auto-hébergement ([#2](https://github.com/betagouv/ComparIA-landing/pull/2)).
- **Architecture logicielle** : Implémentation d'un système de mise en page de base, de composants génériques et de scripts pour l'internationalisation (i18n).
- **Optimisation des performances** : Réduction du poids des pages (RGESN) et optimisation du chargement et de la taille des images.
- **Maintenance** : Résolution de problèmes liés à la séparation du dépôt ([#1](https://github.com/betagouv/ComparIA-landing/pull/1)) et nettoyage de l'architecture.

### Autres changements
- **Documentation** : Ajout et réorganisation du fichier README.
- **Configuration** : Ajout du fichier `yarn.lock`.
