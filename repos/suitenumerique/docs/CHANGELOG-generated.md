## Changelog : docs (30 derniers jours, au 01 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment en matière d'accessibilité, de recherche et de gestion des documents. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la documentation et de la configuration.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur dans l'interface ([#2463](https://github.com/suitenumerique/docs/issues/2463)).
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches.
- Possibilité de créer des sous-documents à partir d'un document existant.
- Ajout d'un bouton pour créer des sous-documents.
- Ajout de la possibilité de quitter un document.
- Ajout d'un support pour les liens "mailto" dans le menu d'aide.
- Ajout d'un sous-menu légal configurable dans le menu d'aide.
- Amélioration de la recherche avec l'ajout du document parent supérieur.
- Limitation du nombre de réactions distinctes par commentaire.

### Évolutions techniques
- Mise à jour de la méthode de suppression d'un utilisateur pour gérer correctement les relations associées.
- Refonte de la suppression d'un utilisateur dans l'interface d'administration.
- Utilisation de l'ID utilisateur au lieu de la relation utilisateur dans le module de partage.
- Amélioration des performances de l'arbre de navigation des documents.
- Correction d'un problème de rechargement de la page lors du focus sur un onglet.
- Correction d'un problème de positionnement du composant Waffle.
- Correction d'un problème de crash lors de l'affichage de threads orphelins.
- Correction d'un problème de chargement de contenu asynchrone sous ASGI.
- Préchargement de l'arbre des commentaires d'un thread pour éviter les requêtes N+1.
- Correction d'un problème de restauration de la suppression héritée.
- Correction d'un problème empêchant le propriétaire de quitter un document supprimé.
- Montée du certificat CA personnalisé dans le déploiement yprovider (helm).
- Mise à jour de la gestion des conversions HTML/Markdown pour préserver les éléments spécifiques (citations, PDF, sauts de page, liens internes, texte commenté).
- Correction d'un test interlinking markdown pour blocknote 0.51.4.
- Correction d'un bug empêchant le stream de chaînes vides avec un itérateur asynchrone sous ASGI.

### Autres changements
- Améliorations de l'accessibilité :
    - Suppression d'un attribut `aria-label` redondant sur les liens de la table des matières.
    - Amélioration de l'accessibilité des composants de recherche.
    - Amélioration de l'accessibilité du mode présentateur.
    - Alignement de l'étiquette du champ de recherche modale avec son espace réservé.
    - Ajout d'IDs aux en-têtes BlockNote pour les ancres de la table des matières.
    - Masquage du panneau latéral mobile pour les lecteurs d'écran lorsqu'il est réduit.
    - Utilisation d'éléments d'en-tête pour le titre de la section des documents épinglés.
    - Utilisation de liens d'ancrage pour les entrées de la table des matières.
    - Focus sur le sélecteur de format dans la modale d'exportation.
    - Piégeage du focus dans le dialogue du présentateur.
    - Annonce de la position de la diapositive en mode présentateur.
- Ajout d'un badge DPG au README.
- Ajout d'un badge Snyk au README.
- Mise à jour des chaînes de traduction.
- Correction de fautes de frappe dans le guide de contribution.
- Suppression de Crisp du projet.
- Mise à jour des dépendances (js et PyJWT).
- Epinglage des dépendances Prosemirror.
- Correction d'un avertissement de sécurité JavaScript.
- Suppression d'un job de test E2E inutile.
- Suppression d'objets créés dans le stockage d'objets pendant les tests.
- Ajout d'un paramètre de configuration manquant CONVERSION_UPLOAD_ENABLED.
- Publication des versions 5.2.0, 5.2.1 et 5.3.0.
