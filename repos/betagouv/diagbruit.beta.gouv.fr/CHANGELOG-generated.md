## Changelog : diagbruit.beta.gouv.fr (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en intégrant un suivi analytique via Matomo, en optimisant l'interface utilisateur et en corrigeant des bugs liés à l'affichage et à la recherche. Des améliorations ont également été apportées à la gestion du contenu de la page d'accueil via Strapi.

### Évolutions fonctionnelles
- Ajout d'un plugin Matomo pour le suivi des interactions utilisateurs via des heatmaps [#78](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/78).
- Amélioration de la recherche par parcelle : suppression de l'adresse dans l'URL après la recherche [#76](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/76).
- Refonte de la présentation des réglementations : suppression du lien sur la description et amélioration de la vérification de la catégorie et du texte [#72](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/72).
- Ajout d'un indicateur de chargement pour l'onglet des recommandations.
- Amélioration de la logique du bouton de recherche.
- Optimisation de la prévisualisation du diagnostic (diagPreview) : chargement dynamique du contenu, optimisation des performances et ajout d'images de remplacement.
- Intégration du contenu de la page d'accueil via Strapi, permettant une gestion plus facile du contenu éditorial [#61](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/61).
- Ajout de trackers Matomo pour le suivi des recherches d'adresses et d'autres interactions utilisateurs [#61](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/61).
- Correction d'un bug empêchant le fonctionnement des liens "FakeLinks".
- Correction de problèmes d'alignement et de taille des éléments sur la page d'accueil.

### Évolutions techniques
- Correction de problèmes de typage dans la classe RegulationCls [#77](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/77).
- Suppression de la source PLU codée en dur pour la réglementation locale [#69](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/69).
- Amélioration de la sécurité concernant la réception des emails de diagnostic [#65](https://github.com/betagouv/diagbruit.beta.gouv.fr/pulls/65).
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Correction de problèmes liés au hoisting de CSS dans certains composants.

### Autres changements
- Mise à jour de la version du projet de 0.1.0 à 0.1.2.
- Correction de fautes de frappe dans le contenu de la page d'accueil.
- Amélioration de la gestion des images et des URLs.
- Correction de bugs mineurs liés à l'affichage et au comportement de certains composants.
