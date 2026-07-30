## Changelog : docs (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment avec l'ajout d'un menu utilisateur, des améliorations de l'interface pour la présentation et la gestion des documents, ainsi que des corrections de bugs pour une meilleure stabilité. Des améliorations de la documentation et des corrections de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un menu utilisateur pour une meilleure gestion du profil et des paramètres [#2463].
- Possibilité d'ouvrir et de partager une présentation à une diapositive spécifique [#2516].
- Amélioration de l'interface utilisateur du panneau latéral gauche, notamment pour l'exportation [#2516].
- Ajout d'une diapositive de titre générée avant le contenu lors de l'utilisation du mode présentateur [#2516].
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches [#2407].
- Ajout d'une commande de gestion pour réinitialiser un document [#1882].
- Restauration du lien "Passer au contenu" après la refonte de l'en-tête [#2510].
- Ajout de nouvelles langues (eo_PL et zh_TW) et renommage de cn_CN en zh_CN [#2486].

### Évolutions techniques
- Adaptation de la commande de construction du `y-provider` suite à une mise à jour de `tsc-alias` [#2516].
- Mise à jour de la configuration de Helm pour monter un certificat CA personnalisé dans le déploiement `yprovider` [#2437].
- Suppression du backend d'authentification par défaut inutilisé [#2480].
- Modification de la recherche de documents pour utiliser l'ID du document au lieu de son chemin [#2501].
- Correction d'une erreur de pointeur nul dans la liste des tâches en arrière-plan (backend_conjob_list) [#2507].
- Amélioration de la gestion de la connexion de collaboration pour une meilleure résilience [#2507].
- Utilisation d'éléments `<p>` sémantiques dans la carte d'informations du document pour l'accessibilité [#2521].
- Refonte de l'en-tête avec une barre flottante pour une meilleure expérience utilisateur et réactivité [#2471].
- Extraction d'un composant de contenu de diapositive de présentateur réutilisable [#2516].
- Refactorisation du présentateur pour utiliser un store unique et un point de montage [#2516].

### Autres changements
- Mise à jour de la documentation pour expliquer la configuration du format de conversion et l'utilisation de S3 [#2481].
- Ajout de modèles de formulaires pour les issues [#2207].
- Suppression de Crisp (outil de chat) et configuration du sous-menu "Légal" dans le menu d'aide [#2416].
- Ajout d'une animation Lottie à la barre flottante de l'en-tête [#2516].
- Correction de tests d'intégration pour l'exportation [#2516].
- Correction de problèmes de focus sur les diapositives du présentateur [#2516].
- Correction de bugs et améliorations de l'interface utilisateur pour préparer la publication 5.4.0 [#2516].
- Ajout de la configuration de l'IA au fichier `.gitignore` [#2516].
- Correction de problèmes de redirection après la suppression d'un document [#2490].
- Amélioration de l'UX du bouton "Importer" sur mobile [#2502].
- Mise à jour des chaînes de traduction [#2498].
