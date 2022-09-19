# coding: utf-8

import os

from django.http import HttpResponse, HttpResponseNotFound

from .mime import MIME

__all__ = (
    'XSendFile',
)


class XSendFile:
    @staticmethod
    def get_filesize(file_path): return os.path.getsize(file_path)

    @staticmethod
    def get_filename(file_path): return os.path.basename(file_path)

    @staticmethod
    def get_extension(file_path):
        _, extension = os.path.splitext(XSendFile.get_filename(file_path))
        print(_, extension)
        return extension

    @staticmethod
    def get_mime(file_path):
        extension = XSendFile.get_extension(file_path)
        return MIME.get(extension, 'application/octet-stream')

    @classmethod
    def serve_file(cls, file_path, redirect_path=None, games_path=None, buffering=True):
        redirect_nginx_file_path = os.path.join(redirect_path, file_path)
        games_file_path = os.path.join(games_path, file_path)

        if not os.path.exists(games_file_path):
            return HttpResponseNotFound('file not found')

        response = HttpResponse()

        response['X-Accel-Redirect'] = os.path.join(redirect_nginx_file_path, '') if os.path.isdir(
            games_file_path) else redirect_nginx_file_path
        # response['X-Accel-Buffering'] = 'on' if buffering else 'off'
        response['Content-Type'] = cls.get_mime(os.path.join(
            games_file_path, "index.html") if os.path.isdir(games_file_path) else games_file_path)
        response['Content-Length'] = cls.get_filesize(os.path.join(
            games_file_path, "index.html") if os.path.isdir(games_file_path) else games_file_path)
        return response
