## Changelog : docs (30 derniers jours, au 2026-07-23)

### Résumé
Ce changelog présente les améliorations apportées à la documentation de Docs au cours du dernier mois. Les principales évolutions concernent l'expérience utilisateur de la présentation (partage de liens, navigation), des corrections de bugs et des améliorations de l'interface utilisateur, ainsi que des mises à jour de la documentation elle-même.

### Évolutions fonctionnelles
- Possibilité d'ouvrir et de partager une présentation à une diapositive spécifique. [#2508](https://github.com/suitenumerique/docs/issues/2508)
- Ajout d'un menu utilisateur pour gérer le profil et les paramètres.
- Amélioration de l'interface utilisateur du panneau latéral.
- Ajout d'une animation Lottie à la barre flottante de l'en-tête.
- Nouvelle barre d'en-tête et harmonisation de la réactivité.
- Possibilité de réinitialiser un document via une commande de gestion.
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches.
- Ajout de la possibilité de quitter un document.
- Ajout d'un bouton "Importer" masqué sur un document.

### Évolutions techniques
- Mise à jour de la version de Next.js vers la 16.2.11 (correction de sécurité).
- Adaptation de la commande de build pour tenir compte d'une mise à niveau de `tsc-alias`.
- Mise à jour de la dépendance `fetch-mock` vers la version 12.6.0.
- Rétrogradation de TypeScript vers la version 6.0.3.
- Rétrogradation des paquets AI vers une version précédente.
- Amélioration de la gestion des erreurs dans le `y-provider` avec l'envoi des erreurs à Sentry.
- Refactorisation du code pour extraire un composant de contenu de diapositive de présentateur réutilisable.
- Refactorisation de l'architecture du présentateur pour utiliser un store et un point de montage unique.
- Modification de la recherche de documents pour utiliser l'ID du document au lieu de son chemin.
- Suppression d'un backend d'authentification par défaut inutilisé.
- Correction d'un pointeur nul dans la liste des tâches de fond du backend Helm.
- Configuration de la journalisation avec la propagation définie sur True.
- Monture du certificat CA personnalisé dans le déploiement yprovider.

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3.
- Correction de fautes de frappe dans le guide de contribution.
- Utilisation d'éléments `<p>` sémantiques dans la carte d'informations du document pour l'accessibilité.
- Correction du positionnement du Waffle.
- Correction du problème de rechargement de l'onglet lors de la mise au point sur l'onglet dans le service worker.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Ajout de locales zh_CN, eo_PL et zh_TW.
- Amélioration de l'accessibilité en supprimant les attributs aria redondants.
- Ajout de modèles de formulaire pour les issues.
- Correction de l'UI/UX du panneau de gauche.
- Correction du bug de l'arborescence DND sur Firefox.
- Mise à jour des chaînes traduites.
- Correction de l'animation Lottie.
- Amélioration de l'accessibilité de la table des matières.
- Correction du CTA sur la modale de déplacement sur mobile.
- Correction du problème de redirection forcée vers l'index lors de la suppression d'un document.
- Ajout de la possibilité de restaurer la capacité de suppression héritée.
- Correction d'un bug empêchant le propriétaire de quitter un document supprimé en douceur.
- Correction de l'UI du panneau de gauche.
- Correction de l'UI/UX avant la publication.
- Correction du bug de l'élément supprimé dans l'arborescence.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction de la position du Waffle.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
- Correction de l'outline de focus sur les diapositives du présentateur.
- Correction du bug de positionnement du Waffle.
- Correction du bug du service worker provoquant un rechargement lors de la mise au point sur l'onglet.
