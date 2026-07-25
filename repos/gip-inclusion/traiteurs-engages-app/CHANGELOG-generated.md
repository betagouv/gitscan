## Changelog : traiteurs-engages-app (30 derniers jours, au 01 juillet 2026)

### Résumé
Les dernières mises à jour améliorent significativement la gestion des demandes de devis pour les administrateurs, avec la possibilité de les modifier ou d'annuler même après leur envoi aux traiteurs. La messagerie a été enrichie avec la possibilité d'ajouter des pièces jointes sécurisées. Des améliorations SEO ont également été apportées avec la publication de nouvelles pages d'articles.

### Évolutions fonctionnelles
- **Messagerie :** Ajout de la possibilité de joindre des images et des fichiers PDF aux messages, avec un téléchargement sécurisé. [#101](https://github.com/gip-inclusion/traiteurs-engages-app/issues/101)
- **Gestion des devis (Admin) :** Les administrateurs peuvent désormais modifier une demande de devis même après son envoi aux traiteurs. [#119](https://github.com/gip-inclusion/traiteurs-engages-app/issues/119)
- **Gestion des devis (Admin) :** Les administrateurs peuvent désormais annuler une demande de devis même après son envoi aux traiteurs, notifiant ainsi l'équipe cliente (créateur et administrateurs). [#120](https://github.com/gip-inclusion/traiteurs-engages-app/issues/120), [#121](https://github.com/gip-inclusion/traiteurs-engages-app/issues/121)
- **Formulaire de demande de devis (Client) :** Amélioration de l'affichage des erreurs spécifiques du formulaire de demande de devis et ajout de logs pour faciliter le débogage. [#125](https://github.com/gip-inclusion/traiteurs-engages-app/issues/125)
- **SEO :** Publication de 4 nouvelles pages d'articles avec un header et footer publics partagés. [#123](https://github.com/gip-inclusion/traiteurs-engages-app/issues/123)
- **SEO :** Ajustements de contenu pour améliorer le référencement de 3 articles. [#124](https://github.com/gip-inclusion/traiteurs-engages-app/issues/124)

### Évolutions techniques
- **Alembic :** Fusion des branches `message-attachments` et `cancellation-reason` pour la gestion des migrations de base de données. [#122](https://github.com/gip-inclusion/traiteurs-engages-app/issues/122)
