## Changelog : agora-back (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des thèmes hebdomadaires, la préparation d'une migration vers Strapi V5, et l'optimisation de l'affichage des réponses et des tendances. Plusieurs corrections et ajustements ont été apportés pour améliorer la qualité des données et l'expérience utilisateur.

### Évolutions fonctionnelles
- Amélioration de l'affichage des thèmes hebdomadaires : ajout de filtres pour afficher les 3 prochains thèmes, gestion de la période optionnelle et affichage dynamique du sous-titre en fonction du type de thème.
- Affichage des réponses : suppression des balises HTML et troncature du texte des réponses pour une meilleure lisibilité.
- Intégration de la transcription textuelle pour les réponses vidéo, permettant d'afficher un résumé du contenu.
- Ajout de deux nouveaux champs pour la page de détails QAG gouvernement.
- Nouvelle logique pour l'onglet "Tendances" : affichage des questions ayant reçu plus de 5 "likes" au cours des dernières 24 heures.
- Correction de l'heure de sélection des questions gagnantes, désormais fixée à 10h.
- Amélioration de l'anonymisation des noms d'utilisateur.

### Évolutions techniques
- Préparation de la migration vers Strapi V5 : plan de migration établi, migrations passées en production, ajout d'un header de compatibilité pour les clients V4.
- Refonte de l'algorithme de calcul des tendances avec une formule plus complexe.
- Ajout d'un contrôleur dédié au traitement hebdomadaire pour un lancement en mode administration.
- Mise en cache optimisée des thèmes hebdomadaires avec un cache court.
- Correction de bugs et amélioration de la robustesse du code.
- Ajout de logs pour faciliter le débogage et le suivi des opérations.

### Autres changements
- Correction de wording et amélioration de la clarté des messages.
- Correction d'un bug lié à l'utilisation de la date de début du thème courant pour filtrer les thèmes hebdomadaires suivants.
- Correction d'un bug dans le script de rollback pour les migrations Strapi V5.
- Ajout d'un flag pour désactiver le cache sur les thèmes hebdomadaires en environnement de recette.
- Correction du champ "programme_du_mois" en rich texte.
- Ajout d'un boolean 'estThemeLibre' pour qualifier les thèmes libres.
