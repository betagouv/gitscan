## Changelog : doctorat-gouv (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'accessibilité (RGAA) et l'intégration de la recherche vectorielle Scaleway. De nombreuses corrections ont été apportées pour améliorer l'expérience utilisateur, notamment en matière de navigation au clavier, de contraste des couleurs et de lisibilité pour les lecteurs d'écran. La recherche vectorielle Scaleway a été enrichie avec la détection d'intentions (localisation et financement) et une interface utilisateur améliorée.

### Évolutions fonctionnelles
- Ajout d'un sitemap XML dynamique et d'un fichier robots.txt pour améliorer le référencement SEO.
- Amélioration de la recherche avec l'intégration de la détection d'intentions (localisation et financement) via Scaleway, affichées sous forme de badges et de chips.
- Ajout d'un badge "En cours d'expérimentation" pour la recherche vectorielle Scaleway.
- Possibilité de sélectionner plusieurs intentions Scaleway avec un indicateur visuel.
- Ajout de meta descriptions sur les pages de contact, de recherche et de détail d'une thèse pour améliorer le SEO.
- Amélioration de l'affichage des offres similaires.

### Évolutions techniques
- Désactivation possible du scheduler d'indexation Albert via une propriété.
- Amélioration de la robustesse du split de la requête pour la recherche vectorielle.
- Refactor de la détection des intentions de localisation et de financement.
- Augmentation du budget CSS pour la page de recherche.
- Suppression du suivi git d'un fichier de release.
- Mise à jour des versions pour les releases 0.3.7 et 0.3.8.
- Intégration de logs pour les requêtes vectorielles Scaleway.

### Autres changements
- Nombreuses corrections d'accessibilité (RGAA) : amélioration du focus management, ajout d'attributs ARIA, correction des contrastes de couleurs, amélioration de la navigation au clavier, ajout de labels accessibles, etc.
- Correction de liens et de titres pour améliorer l'accessibilité.
- Amélioration de la formulation des messages d'aide et d'ambiguïté de la recherche vectorielle.
- Correction de l'affichage des badges de type de bloc matche Scaleway.
- Mise à jour de l'exemple NLP pour la recherche vectorielle.
- Correction de l'attribut `lang` du document lors du changement de langue.
- Amélioration de l'affichage des messages d'erreur avec `aria-invalid` et `aria-describedby`.
- Suppression du texte d'exemple NLP et de l'astérisque.
- Ajout d'un lien d'évitement vers le contenu principal.
- Correction de l'affichage des compteurs sur les sections "Meilleurs résultats" et "Autres résultats".
