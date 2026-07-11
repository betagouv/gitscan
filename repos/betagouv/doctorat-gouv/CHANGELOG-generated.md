## Changelog : doctorat-gouv (30 derniers jours, au 10 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la recherche, notamment l'intégration de Scaleway pour la recherche vectorielle et l'amélioration de l'accessibilité (RGAA). Des optimisations de l'interface utilisateur et des corrections de bugs ont également été apportées pour une meilleure expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'une recherche par localisation via Scaleway et pgvector.
- Intégration de filtres Scaleway (6 filtres du formulaire).
- Remplacement d'Albert par un toggle Scaleway avec barre de recherche et aide NLP.
- Amélioration de l'affichage des résultats de recherche avec un carrousel, des compteurs par section et un tri par pertinence par défaut.
- Ajout de badges d'intentions (localisation, financement) et de chips pour une meilleure visualisation des critères de recherche.
- Ajout d'un message d'aide NLP pour guider l'utilisateur dans la formulation de sa recherche.
- Ajout d'un sitemap XML dynamique et d'un fichier robots.txt pour améliorer le SEO.
- Ajout de meta descriptions sur les pages de contact, de recherche et de détail d'une thèse pour le SEO.
- Amélioration de la gestion du focus et de l'accessibilité des filtres (RGAA).
- Correction de contrastes critiques des couleurs custom (RGAA).
- Ajout d'aria-label aux boutons de suppression de filtres (RGAA).
- Amélioration de l'accessibilité de la page détail (alertes dynamiques, liens target=_blank) (RGAA).
- Ajout de régions live ARIA pour les mises à jour dynamiques (RGAA).
- Correction de liens "Aller au contenu principal" (RGAA).
- Ajout de titres et de balises `main` sur les pages détail et contact (RGAA).
- Correction de l'association des labels aux champs du formulaire de contact (RGAA).
- Ajout de titres aux messages d'erreur (RGAA).
- Ajout de l'état actif des boutons switch et tri par aria-pressed (RGAA).
- Ajout d'un lien d'évitement vers le contenu principal (RGAA).

### Évolutions techniques
- Intégration de Scaleway pour la recherche vectorielle.
- Amélioration de la détection des intentions de localisation et de financement.
- Refactor de la logique de scan des intentions.
- Suppression du cap à 85% du score composite Scaleway.
- Mise à jour des versions pour la release 0.3.8 et 0.3.7.
- Ajout de logs pour les requêtes vectorielles Scaleway.
- Suppression du scheduler d'indexation Albert via une propriété.
- Augmentation du budget CSS pour la page de recherche.
- Correction de la robustesse du split de la requête.
- Ajout de tests et de corrections pour l'accessibilité (RGAA).

### Autres changements
- Ajout de la documentation MODOP pour la release v0.3.7.
- Mise à jour de l'exemple NLP pour la recherche vectorielle.
- Correction du suivi git dans un fichier de documentation.
- Suppression d'un texte d'exemple NLP et de son astérisque.
- Reformulation des messages d'aide et d'ambiguïté de la recherche vectorielle.
- Correction de l'attribut `lang` du document lors du changement de langue.
- Suppression du badge de type de bloc matche Scaleway sur les titres.
- Amélioration de la détection des localisations insensible à la casse.
- Correction de la hiérarchie de titres.
- Ajout de labels accessibles aux champs de recherche des dropdowns.
- Remplacement des flèches du carrousel par des boutons DSFR tertiaires.
- Remplacement des points du carrousel par des flèches de navigation en bas.
- Harmonisation du style du titre de la section 2 avec celui de la section 1.
- Ajout du compteur de filtres actifs pour activer le bouton reset.
- Tri par pertinence uniquement en mode IA, date par défaut en recherche standard.
- Suppression des compteurs sur les chips d'intentions.
- Ajout de la sélection multiple des intentions Scaleway avec indicateur visuel.
- Validation de la fiabilité des intentions détectées avant affichage.
- Amélioration de l'UI de la recherche vectorielle (chargement Scaleway, chips actifs visibles, compteurs, tooltip custom).
- Correction de l'affichage des badges de score Scaleway.
- Suppression du cap a 85% du score composite Scaleway.
- Ajout d'un log des requêtes vectorielles en base avec flag d'activation.
- Correction de l'affichage des messages ambigus.
- Ajout de l'attribut `title` aux liens des mentions légales du contact (RGAA).
- Ajout d'un titre dynamique à la page en fonction du contexte.
- Ajout d'un badge "En cours d'expérimentation" à la recherche vectorielle.
- Suppression des compteurs sur les sections "Meilleurs résultats" et "Autres résultats".
- Correction de l'affichage de la section "Offres qui pourraient également vous intéresser".
- Suppression du badge de type de bloc matche Scaleway également dans la section carrousel.
